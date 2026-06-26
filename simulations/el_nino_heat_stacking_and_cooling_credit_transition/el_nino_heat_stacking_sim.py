"""Conceptual El Nino heat-stacking and Cooling Credit transition simulation.

This is not a precise climate forecast. It is a deterministic, index-based
counterfactual model for comparing policy pathways and heat-load dynamics
under El Nino risk from 2015 to 2035.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt


YEARS = list(range(2015, 2036))
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


@dataclass(frozen=True)
class Scenario:
    key: str
    name: str
    carbon_start: float
    carbon_slope: float
    carbon_post_2026_bonus: float
    cooling_start: float
    cooling_slope_pre_2026: float
    cooling_slope_post_2026: float
    natural_recovery_post_2026: float
    direct_heat_relief_post_2026: float


SCENARIOS = [
    Scenario(
        "A",
        "Carbon Credit Baseline",
        carbon_start=42,
        carbon_slope=1.1,
        carbon_post_2026_bonus=0.1,
        cooling_start=8,
        cooling_slope_pre_2026=0.2,
        cooling_slope_post_2026=0.3,
        natural_recovery_post_2026=0.15,
        direct_heat_relief_post_2026=0.1,
    ),
    Scenario(
        "B",
        "Stronger Carbon Mitigation",
        carbon_start=44,
        carbon_slope=1.7,
        carbon_post_2026_bonus=0.5,
        cooling_start=9,
        cooling_slope_pre_2026=0.25,
        cooling_slope_post_2026=0.45,
        natural_recovery_post_2026=0.25,
        direct_heat_relief_post_2026=0.25,
    ),
    Scenario(
        "C",
        "Cooling Credit Transition",
        carbon_start=43,
        carbon_slope=1.25,
        carbon_post_2026_bonus=0.3,
        cooling_start=10,
        cooling_slope_pre_2026=0.35,
        cooling_slope_post_2026=3.2,
        natural_recovery_post_2026=2.2,
        direct_heat_relief_post_2026=2.1,
    ),
    Scenario(
        "D",
        "Cooling Credit Acceleration",
        carbon_start=43,
        carbon_slope=1.35,
        carbon_post_2026_bonus=0.4,
        cooling_start=11,
        cooling_slope_pre_2026=0.45,
        cooling_slope_post_2026=4.9,
        natural_recovery_post_2026=3.4,
        direct_heat_relief_post_2026=3.2,
    ),
]


def clamp(value: float, low: float = 0, high: float = 100) -> float:
    return max(low, min(high, value))


def el_nino_pulse(year: int) -> float:
    """Stylized heat pulse years used to test background heat-load sensitivity."""
    pulses = {
        2015: 8,
        2016: 12,
        2019: 5,
        2023: 9,
        2024: 12,
        2027: 6,
        2030: 10,
        2034: 8,
        2035: 5,
    }
    return pulses.get(year, 0)


def ramp_after(year: int, start_year: int = 2026) -> int:
    return max(0, year - start_year + 1)


def simulate_scenario(scenario: Scenario) -> list[dict[str, float | int | str]]:
    rows: list[dict[str, float | int | str]] = []

    for i, year in enumerate(YEARS):
        post = ramp_after(year)
        warming_pressure = i * 1.65
        carbon_policy = clamp(
            scenario.carbon_start
            + scenario.carbon_slope * i
            + scenario.carbon_post_2026_bonus * post
        )
        cooling_policy = clamp(
            scenario.cooling_start
            + scenario.cooling_slope_pre_2026 * min(i, 10)
            + scenario.cooling_slope_post_2026 * post
        )
        cooling_intervention = clamp(0.88 * cooling_policy + 0.05 * carbon_policy)

        natural_recovery_base = 30 - 0.45 * i
        soil_moisture = clamp(
            natural_recovery_base
            + 0.42 * cooling_intervention
            + scenario.natural_recovery_post_2026 * post
        )
        forest_evapotranspiration = clamp(
            34
            - 0.35 * i
            + 0.36 * cooling_intervention
            + 0.85 * scenario.natural_recovery_post_2026 * post
        )
        water_cycle = clamp(0.48 * soil_moisture + 0.42 * forest_evapotranspiration + 0.10 * cooling_intervention)
        ocean_circulation = clamp(
            29
            - 0.32 * i
            + 0.30 * cooling_intervention
            + 0.70 * scenario.natural_recovery_post_2026 * post
        )
        natural_cooling = clamp(
            0.28 * soil_moisture
            + 0.28 * forest_evapotranspiration
            + 0.24 * water_cycle
            + 0.20 * ocean_circulation
        )

        carbon_heat_relief = 0.13 * carbon_policy
        direct_heat_relief = scenario.direct_heat_relief_post_2026 * post + 0.34 * cooling_intervention
        accumulated_ocean_heat = clamp(57 + 1.45 * i + 0.45 * el_nino_pulse(year) - 0.16 * direct_heat_relief - 0.08 * natural_cooling)
        heat_inertia = clamp(0.64 * accumulated_ocean_heat + 0.22 * (100 - natural_cooling) + 0.14 * warming_pressure)
        climate_time_lag = clamp(0.58 * heat_inertia + 0.26 * accumulated_ocean_heat - 0.10 * cooling_intervention)
        natural_cooling_recovery = clamp(0.40 * natural_cooling + 0.24 * soil_moisture + 0.20 * water_cycle + 0.16 * ocean_circulation)
        direct_cooling_intervention = clamp(0.72 * cooling_intervention + 0.28 * direct_heat_relief)
        ocean_heat_load = clamp(
            49
            + warming_pressure
            + 0.75 * el_nino_pulse(year)
            + 0.12 * heat_inertia
            - 0.24 * natural_cooling
            - 0.34 * direct_heat_relief
            - carbon_heat_relief
        )
        existing_heat_load = clamp(
            0.46 * accumulated_ocean_heat
            + 0.24 * ocean_heat_load
            + 0.18 * (47 + 1.25 * i)
            + 0.12 * climate_time_lag
            - 0.18 * direct_cooling_intervention
        )
        sea_surface_temp_risk = clamp(0.78 * ocean_heat_load + 0.95 * el_nino_pulse(year) + 8)
        urban_heat = clamp(
            47
            + 1.25 * i
            + 0.28 * el_nino_pulse(year)
            - 0.44 * cooling_intervention
            - 0.20 * water_cycle
        )
        wbgt_land = clamp(0.58 * urban_heat + 0.28 * ocean_heat_load + 0.20 * el_nino_pulse(year) + 5)
        food_water = clamp(0.43 * wbgt_land + 0.35 * (100 - soil_moisture) + 0.22 * (100 - water_cycle))
        marine_heatwave = clamp(0.63 * sea_surface_temp_risk + 0.31 * ocean_heat_load - 0.18 * ocean_circulation)
        coral_bleaching = clamp(0.74 * marine_heatwave + 0.18 * sea_surface_temp_risk - 0.10 * ocean_circulation)
        el_nino_heat_stacking = clamp(
            0.30 * ocean_heat_load
            + 0.22 * sea_surface_temp_risk
            + 0.18 * wbgt_land
            + 0.14 * food_water
            + 0.16 * (100 - natural_cooling)
        )
        thermal_accounting = clamp(
            0.30 * cooling_policy
            + 0.24 * direct_cooling_intervention
            + 0.22 * natural_cooling_recovery
            + 0.14 * water_cycle
            + 0.10 * ocean_circulation
        )

        rows.append(
            {
                "year": year,
                "scenario": scenario.name,
                "carbon_credit_policy_index": round(carbon_policy, 2),
                "cooling_credit_policy_index": round(cooling_policy, 2),
                "accumulated_ocean_heat_index": round(accumulated_ocean_heat, 2),
                "heat_inertia_index": round(heat_inertia, 2),
                "climate_time_lag_index": round(climate_time_lag, 2),
                "existing_heat_load_index": round(existing_heat_load, 2),
                "ocean_heat_load_index": round(ocean_heat_load, 2),
                "sea_surface_temperature_risk_index": round(sea_surface_temp_risk, 2),
                "el_nino_heat_stacking_index": round(el_nino_heat_stacking, 2),
                "marine_heatwave_risk_index": round(marine_heatwave, 2),
                "coral_bleaching_risk_index": round(coral_bleaching, 2),
                "wbgt_land_heat_risk_index": round(wbgt_land, 2),
                "food_water_stress_index": round(food_water, 2),
                "urban_heat_load_index": round(urban_heat, 2),
                "soil_moisture_recovery_index": round(soil_moisture, 2),
                "forest_evapotranspiration_recovery_index": round(forest_evapotranspiration, 2),
                "water_cycle_recovery_index": round(water_cycle, 2),
                "ocean_circulation_support_index": round(ocean_circulation, 2),
                "natural_cooling_function_index": round(natural_cooling, 2),
                "cooling_credit_intervention_index": round(cooling_intervention, 2),
                "direct_cooling_intervention_index": round(direct_cooling_intervention, 2),
                "natural_cooling_recovery_index": round(natural_cooling_recovery, 2),
                "thermal_accounting_index": round(thermal_accounting, 2),
            }
        )

    return rows


def write_csv(rows: list[dict[str, float | int | str]]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with (OUTPUT_DIR / "simulation_results.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def series(rows: list[dict[str, float | int | str]], scenario: str, column: str) -> list[float]:
    return [float(row[column]) for row in rows if row["scenario"] == scenario]


def plot_lines(rows: list[dict[str, float | int | str]], columns: list[str], title: str, ylabel: str, filename: str) -> None:
    plt.figure(figsize=(11, 6.2))
    for scenario in SCENARIOS:
        values = series(rows, scenario.name, columns[0])
        label = scenario.name if len(columns) == 1 else f"{scenario.name}: {columns[0].replace('_index', '').replace('_', ' ')}"
        plt.plot(YEARS, values, linewidth=2.4, label=label)
        for extra in columns[1:]:
            plt.plot(
                YEARS,
                series(rows, scenario.name, extra),
                linewidth=1.5,
                linestyle="--",
                alpha=0.75,
                label=f"{scenario.name}: {extra.replace('_index', '').replace('_', ' ')}",
            )
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel("Year")
    plt.ylim(0, 100)
    plt.grid(True, alpha=0.25)
    plt.legend(fontsize=8, ncol=2)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=180)
    plt.close()


def plot_policy_response(rows: list[dict[str, float | int | str]]) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.6), sharey=True)
    for scenario in SCENARIOS:
        axes[0].plot(YEARS, series(rows, scenario.name, "carbon_credit_policy_index"), linewidth=2.2, label=scenario.name)
        axes[1].plot(YEARS, series(rows, scenario.name, "cooling_credit_policy_index"), linewidth=2.2, label=scenario.name)
    axes[0].set_title("Carbon Credit policy index")
    axes[1].set_title("Cooling Credit policy index")
    for ax in axes:
        ax.set_xlabel("Year")
        ax.set_ylim(0, 100)
        ax.grid(True, alpha=0.25)
    axes[0].set_ylabel("Normalized index (0-100)")
    axes[1].legend(fontsize=8)
    fig.suptitle("Carbon-credit accounting improves earlier; cooling-credit response rises after transition")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "carbon_credit_vs_cooling_credit_response.png", dpi=180)
    plt.close(fig)


def plot_causal_loop() -> None:
    labels = [
        "Accumulated ocean heat",
        "El Nino heat pulse",
        "Marine heatwaves",
        "WBGT and land heat",
        "Food and water stress",
        "Weakened natural cooling",
        "Cooling Credit interventions",
        "Thermal accounting",
    ]
    points = [
        (0.50, 0.90),
        (0.82, 0.72),
        (0.78, 0.40),
        (0.48, 0.20),
        (0.18, 0.38),
        (0.18, 0.70),
        (0.50, 0.52),
        (0.50, 0.70),
    ]
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    for label, (x, y) in zip(labels, points):
        ax.text(
            x,
            y,
            label,
            ha="center",
            va="center",
            fontsize=10,
            bbox=dict(boxstyle="round,pad=0.35", facecolor="#f7fbff", edgecolor="#2a6f97", linewidth=1.5),
        )
    arrows = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (7, 6), (6, 5), (6, 3), (6, 0)]
    for a, b in arrows:
        ax.annotate(
            "",
            xy=points[b],
            xytext=points[a],
            arrowprops=dict(arrowstyle="->", color="#264653", lw=1.6, shrinkA=22, shrinkB=22),
        )
    ax.set_title("Conceptual feedback loop: heat stacking and cooling-credit intervention")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "causal_feedback_loop.png", dpi=180)
    plt.close(fig)


def make_plots(rows: list[dict[str, float | int | str]]) -> None:
    plot_lines(rows, ["el_nino_heat_stacking_index"], "El Nino heat-stacking index", "Risk index (0-100)", "el_nino_heat_stacking_index.png")
    plot_policy_response(rows)
    plot_lines(rows, ["ocean_heat_load_index", "accumulated_ocean_heat_index", "existing_heat_load_index"], "Ocean heat-load pathways and heat inertia", "Heat-load index (0-100)", "ocean_heat_load_pathways.png")
    plot_lines(rows, ["marine_heatwave_risk_index", "coral_bleaching_risk_index"], "Marine heatwave and coral bleaching risk", "Risk index (0-100)", "marine_heatwave_risk_index.png")
    plot_lines(rows, ["wbgt_land_heat_risk_index", "urban_heat_load_index"], "WBGT and land heat risk", "Risk index (0-100)", "wbgt_and_land_heat_risk_index.png")
    plot_lines(rows, ["natural_cooling_function_index", "natural_cooling_recovery_index", "soil_moisture_recovery_index", "water_cycle_recovery_index"], "Natural cooling recovery", "Recovery index (0-100)", "natural_cooling_recovery_index.png")
    plot_lines(rows, ["cooling_credit_intervention_index", "direct_cooling_intervention_index", "thermal_accounting_index"], "Cooling Credit transition effect", "Intervention index (0-100)", "cooling_credit_transition_effect.png")
    plot_causal_loop()


def main() -> None:
    rows: list[dict[str, float | int | str]] = []
    for scenario in SCENARIOS:
        rows.extend(simulate_scenario(scenario))
    write_csv(rows)
    make_plots(rows)
    print(f"Wrote {len(rows)} rows and PNG outputs to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
