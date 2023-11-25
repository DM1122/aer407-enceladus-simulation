"""Suborbital hop governing equations"""

from astropy import units as u
import numpy as np


def range_of_hop(v0: u.m / u.s, theta: u.deg, g: u.m / u.s**2, v_tilde: float) -> u.m:
    """
    Calculate total range between launch and impact sites.

    Parameters:
        v0: Launch velocity
        theta: Launch elevation angle
        g: Surface gravity of the planetary body
        v_tilde: Launch velocity relative to the first cosmic velocity

    Returns:
        Total range between launch and impact sites.
    """
    return (v0**2 * np.sin(2 * np.radians(theta)) / g) / np.sqrt(
        1 - (2 - v_tilde**2) * v_tilde**2 * np.cos(np.radians(theta)) ** 2
    )


def max_range(v0: u.m / u.s, g: u.m / u.s**2, v_tilde: float) -> u.m:
    """
    Calculate maximum range of projectile launched at optimal launch angle.

    Parameters:
        v0: Launch velocity
        g: Surface gravity of the planetary body
        v_tilde: Launch velocity relative to the first cosmic velocity

    Returns:
        Maximum range of projectile launched at optimal launch angle.
    """
    return (v0**2 / g) / (1 - 0.5 * v_tilde**2)


def launch_velocity_from_max_range(d_max: u.m, R: u.m, g: u.m / u.s**2) -> u.m / u.s:
    """
    Calculate the neccessary launch velocity to travel a given distance, assuming optimal launch angle.

    Parameters:
        d_max: Range
        R: Radius of planet
        g: Planet's gravity

    Returns:
        Launch velocity to travel a given distance
    """

    v = np.sqrt((d_max * R * g**2) / (R * g + 0.5 * d_max * g))

    return v.decompose()


def launch_relative_velocity(v0: u.m / u.s, R: u.m, g: u.m / u.s**2) -> float:
    """
    Calculate launch velocity relative to the first cosmic velocity.

    Parameters:
        v0: Launch velocity
        R: Radius of the planetary body
        g: Surface gravity of the planetary body

    Returns:
        Relative launch velocity.
    """
    return v0 / np.sqrt(R * g)


def optimum_launch_angle(v_tilde: float) -> u.deg:
    """
    Calculate optimum launch elevation angle.

    Parameters:
        v_tilde: Launch velocity relative to the first cosmic velocity

    Returns:
        Optimum launch elevation angle.
    """
    theta = 0.5 * np.arccos(v_tilde**2 / (2 - v_tilde**2))

    return theta.to(u.deg)


def max_height(v0: u.m / u.s, theta: u.deg, g: u.m / u.s**2, v_tilde: float) -> u.m:
    """
    Calculate maximum height of a projectile above the planetary surface.

    Parameters:
        v0: Launch velocity
        theta: Launch elevation angle
        g: Surface gravity of the planetary body
        v_tilde: Launch velocity relative to the first cosmic velocity

    Returns:
        Maximum height of a projectile above the planetary surface.
    """
    term1 = v0**2 * np.sin(np.radians(theta)) ** 2 / g
    term2 = 1 - v_tilde**2
    term3 = np.sqrt(
        1 - (2 - v_tilde**2) * v_tilde**2 * np.cos(np.radians(theta)) ** 2
    )
    return term1 / (term2 + term3)


def time_of_flight(
    v0: u.m / u.s, theta: u.deg, g: u.m / u.s**2, v_tilde: float
) -> u.s:
    """
    Calculate time of flight.

    Parameters:
        v0: Launch velocity
        theta: Launch angle
        g: Surface gravity of the planetary body
        v_tilde: Launch velocity relative to the first cosmic velocity

    Returns:
        Time of flight.
    """
    term1 = 2 * v0 * np.sin(np.radians(theta)) / g
    term2 = 1 / (2 - v_tilde**2)
    term3 = np.sqrt(2 - v_tilde**2) * v_tilde * np.sin(np.radians(theta))
    term4 = np.sqrt(
        1 - (2 - v_tilde**2) * v_tilde**2 * np.cos(np.radians(theta)) ** 2
    )
    term5 = 1 + (1 / term3) * np.arcsin(term3 / term4)
    return term1 * term2 * term5


def launch_velocity_from_delta_v(dV: u.m / u.s) -> u.m / u.s:
    """
    Calculate launch velocity from delta-V.

    Parameters:
        dV: Delta-V

    Returns:
        Resulting launch velocity.
    """
    return 0.5 * dV


def hop_delta_v(v0: u.m / u.s) -> u.m / u.s:
    """
    Calculate the required delta-v for a hop of a given launch velocity

    Parameters:
        v0: Launch velocity

    Returns:
        Required delta-v
    """
    return 2 * v0


def delta_v_from_launch_velocity(v0: u.m / u.s) -> u.m / u.s:
    """
    Calculate delta-V required for a given launch velocity.

    Parameters:
        v0: Launch velocity

    Returns:
        Resulting launch velocity.
    """
    return 2 * v0


def fuel_mass(delta_v: u.m / u.s, v_e: u.m / u.s, m_f: u.kg) -> float:
    """
    Calculate fuel mass

    Parameters:
        delta_v: Change in velocity
        v_e: Exhaust velocity
        m_f: Final (dry) mass

    Returns:
        Percent fuel mass.
    """
    mp = m_f * np.exp(delta_v / v_e) - m_f

    return mp


def fuel_mass_percent(delta_v: u.m / u.s, v_e: u.m / u.s, m_f: u.kg) -> float:
    """
    Calculate fuel mass percent.

    Parameters:
        delta_v: Change in velocity
        v_e: Exhaust velocity
        m_f: Final (dry) mass

    Returns:
        Percent fuel mass.
    """
    m0 = m_f * np.exp(delta_v / v_e)

    return ((m0 - m_f) / m0 * 100) * u.percent
