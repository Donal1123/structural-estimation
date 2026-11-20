"""Demand calculations for one random coefficient in the course's BLP model."""

import numpy as np
from scipy.special import logsumexp, roots_hermitenorm


def normal_quadrature(order):
    """Return Gauss–Hermite nodes and normalized weights for a standard normal."""
    nodes, weights = roots_hermitenorm(order)
    return nodes, weights / weights.sum()


def _log_inside_probabilities(delta, x, sigma, nodes):
    utility = delta[..., None, :] + sigma * nodes[:, None] * x[..., None, :]
    log_denominator = np.logaddexp(0, logsumexp(utility, axis=-1, keepdims=True))
    return utility - log_denominator


def market_probabilities(delta, x, sigma, nodes):
    """Return conditional inside probabilities, indexed by type and product.

    In a single market, delta and x are one vector per product and the result
    has shape (number of nodes, products). Leading market axes are preserved
    when calculating a batch of markets with the same number of products.
    """
    return np.exp(_log_inside_probabilities(np.asarray(delta), np.asarray(x), sigma, nodes))


def invert_shares(observed_shares, x, sigma, nodes, weights, *, tolerance=1e-10, max_iterations=4000):
    """Return delta, number of updates, and the maximum absolute log-share error.

    Each row of observed_shares is a market. All inside and outside shares
    must be strictly positive. Reusing nodes across sigma makes the profiled
    objective deterministic.
    """
    observed_shares = np.asarray(observed_shares, dtype=float)
    x = np.asarray(x, dtype=float)
    if observed_shares.ndim != 2 or x.shape != observed_shares.shape:
        raise ValueError("expected one row per market and aligned product characteristics")
    outside_shares = 1 - observed_shares.sum(axis=1, keepdims=True)
    if not (np.all(observed_shares > 0) and np.all(outside_shares > 0)):
        raise ValueError("BLP inversion requires strictly positive inside and outside shares")

    log_observed = np.log(observed_shares)
    log_weights = np.log(weights)[:, None]
    delta = log_observed - np.log(outside_shares)
    for updates in range(max_iterations + 1):
        log_probabilities = _log_inside_probabilities(delta, x, sigma, nodes)
        log_predicted = logsumexp(log_probabilities + log_weights, axis=-2)
        correction = log_observed - log_predicted
        max_error = np.max(np.abs(correction))
        if max_error <= tolerance:
            return delta, updates, max_error
        delta = delta + correction

    raise RuntimeError(f"share inversion failed after {max_iterations} updates (error {max_error:.2g})")
