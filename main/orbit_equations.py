from astropy import units as u
from astropy import constants as const
import numpy as np
import pandas as pd


def orbit_delta_v(mass: u.kg, radius: u.m, altitude: u.m):
    delta_v_orbit = escape_velocity(mass, radius) - orbit_velocity(
        mass, radius, altitude
    )

    return delta_v_orbit


def escape_velocity(mass, radius):
    v = np.sqrt(2 * const.G * mass / radius)

    return v.decompose()


def orbit_velocity(mass, radius, altitude):
    v = np.sqrt(const.G * mass / (radius + altitude))

    return v.decompose()


def generate_fuel_operations_table(
    num_hops, delta_v_descent, delta_v_hop, delta_v_ascent, dry_mass, fuel_margin, I_sp
):
    """
    Calculate the initial and final mass of a spacecraft for a series of operations:
    descent, a number of suborbital hops, and ascent. The function computes the fuel
    requirements for each operation based on the specified delta-v values, working
    backwards from the ascent.

    The calculations assume that the final mass after all operations is the dry mass of the
    spacecraft plus the given margin and that the fuel is consumed in each operation.
    """
    # Convert specific impulse to effective exhaust velocity
    v_exhaust = I_sp * const.g0.value

    operations = []

    # Start with ascent since it's the final operation, work backwards to calculate the initial mass including fuel
    # Now we keep a margin of fuel at the end of ascent
    mass_final_ascent = dry_mass + fuel_margin
    mass_initial_ascent = mass_final_ascent * np.exp(delta_v_ascent / v_exhaust)
    operations.append(
        {
            "Operation": "Ascent",
            "Initial Mass": mass_initial_ascent,
            "Final Mass": mass_final_ascent,
        }
    )

    # Update the current mass for the hop calculations
    current_mass = mass_initial_ascent

    # Calculate fuel for each hop, working backwards
    for i in range(num_hops, 0, -1):
        mass_final_hop = current_mass
        mass_initial_hop = mass_final_hop * np.exp(delta_v_hop / v_exhaust)
        operations.append(
            {
                "Operation": f"Hop {i}",
                "Initial Mass": mass_initial_hop,
                "Final Mass": mass_final_hop,
            }
        )
        current_mass = mass_initial_hop

    # Calculate fuel for descent, which is the first operation
    mass_final_descent = current_mass
    mass_initial_descent = mass_final_descent * np.exp(delta_v_descent / v_exhaust)
    operations.append(
        {
            "Operation": "Descent",
            "Initial Mass": mass_initial_descent,
            "Final Mass": mass_final_descent,
        }
    )

    # Create a DataFrame from the list of operations and reverse it to show the proper order
    df = pd.DataFrame(operations).iloc[::-1].reset_index(drop=True)

    return df
