from astropy import units as u
from main.hop_equations import (
    launch_relative_velocity,
    range_of_hop,
    max_range,
    optimum_launch_angle,
    max_height,
    time_of_flight,
    launch_velocity_from_delta_v,
    fuel_mass_percent,
    fuel_mass,
    delta_v_from_launch_velocity,
    launch_velocity_from_max_range,
)


def test_range_of_hop():
    """Test if the function returns the correct units."""
    v0 = 10 * u.m / u.s
    theta = 10 * u.degree
    g = 0.113 * u.m / u.s**2
    vtilde = 0.1

    result = range_of_hop(v0, theta, g, vtilde)
    print(result)
    assert result.unit == u.m


def test_max_range():
    """Test if the function returns the correct units."""
    vtilde = 0.019914550754334782
    v0 = 3.361213957824707 * u.m / u.s
    g = 0.113 * u.m / u.s**2

    result = max_range(v0, g, vtilde)
    print(result)
    assert result.unit == u.m


def test_launch_velocity_from_max_range():
    """Test if the function returns the correct units."""
    g = 0.113 * u.m / u.s**2
    R = 252.1 * 1e3 * u.m
    d_max = 100 * u.m

    result = launch_velocity_from_max_range(d_max, R, g)
    print(result)
    assert result.unit == u.m / u.s


def test_launch_relative_velocity():
    """Test if the function returns the correct units."""
    v0 = 3.361213957824707 * u.m / u.s
    g = 0.113 * u.m / u.s**2
    R = 252.1 * 1e3 * u.m

    result = launch_relative_velocity(v0, R, g)
    print(result)
    assert result.unit == u.dimensionless_unscaled


def test_optimum_launch_angle():
    """Test if the function returns the correct units."""
    vtilde = 0.1

    result = optimum_launch_angle(vtilde)
    print(result)
    assert result.unit == u.deg


def test_max_height():
    """Test if the function returns the correct units."""
    v0 = 10 * u.m / u.s
    theta = 10 * u.degree
    g = 0.113 * u.m / u.s**2
    vtilde = 0.1

    result = max_height(v0, theta, g, vtilde)
    print(result)
    assert result.unit == u.m


def test_time_of_flight():
    """Test if the function returns the correct units."""
    v0 = 10 * u.m / u.s
    theta = 10 * u.degree
    g = 0.113 * u.m / u.s**2
    vtilde = 0.1

    result = time_of_flight(v0, theta, g, vtilde)
    print(result)
    assert result.unit == u.s


def test_launch_velocity_from_delta_v():
    """Test if the function returns the correct units."""
    dV = 50 * u.m / u.s

    result = launch_velocity_from_delta_v(dV)
    print(result)
    assert result.unit == u.m / u.s


def test_delta_v_from_launch_velocity():
    """Test if the function returns the correct units."""
    v0 = 50 * u.m / u.s

    result = delta_v_from_launch_velocity(v0)
    print(result)
    assert result.unit == u.m / u.s


def test_fuel_mass():
    """Test if the function returns the correct units."""
    dV = 50 * u.m / u.s
    v_e = 1000 * u.m / u.s
    m_f = 100 * u.kg

    result = fuel_mass(dV, v_e, m_f)
    print(result)
    assert result.unit == u.kg


def test_fuel_mass_percent():
    """Test if the function returns the correct units."""
    dV = 50 * u.m / u.s
    v_e = 1000 * u.m / u.s
    m_f = 100 * u.kg

    result = fuel_mass_percent(dV, v_e, m_f)
    print(result)
    assert result.unit == u.percent
