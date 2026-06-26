# El Nino Heat-Stacking and Cooling Credit Transition Simulation

This module is a conceptual, index-based, counterfactual simulation for comparing climate-policy pathways under El Nino heat-stacking risk from 2015 to 2035.

It is not a precise climate forecast. It is a causal teaching model that asks how different policy frames respond when El Nino occurs on top of accumulated ocean heat, land heat, WBGT risk, soil dryness, and weakened natural cooling functions.

## Core Thesis

El Nino in the age of global warming is not only a meteorological event. It is a warning signal that the Earth system already contains too much accumulated heat, especially in the ocean.

Carbon Credits ask:

```text
How much CO2 was reduced, removed, or offset?
```

Cooling Credits ask:

```text
How much heat load was reduced, avoided, dissipated, or buffered through measurable cooling functions?
```

Carbon credits can support emissions reduction and accounting. However, carbon accounting alone has not sufficiently demonstrated direct, measurable reduction of existing heat loads. It also does not directly evaluate ocean heat, WBGT, surface temperature, soil moisture, evapotranspiration, water-cycle recovery, or marine cooling functions.

Cooling Credits are therefore proposed as a complementary and potentially transitional framework focused on measurable cooling contribution.

## Scenarios

### A. Carbon Credit Baseline

Carbon-credit-centered policy continues. Emissions accounting improves gradually, but direct cooling investment remains weak. Natural cooling functions recover slowly or continue weakening.

### B. Stronger Carbon Mitigation

CO2 mitigation improves more strongly than baseline. However, direct cooling, soil moisture recovery, evapotranspiration recovery, urban cooling, and ocean cooling functions remain insufficient.

### C. Cooling Credit Transition

A portion of climate finance shifts from carbon offset accounting toward measurable cooling contribution. Urban cooling, soil moisture, humus, forest evapotranspiration, water-cycle recovery, and ocean-circulation support increase from 2026 onward.

### D. Cooling Credit Acceleration

Cooling Credits become a major climate-finance category. Large-scale but regionally adapted interventions are deployed for urban heat reduction, WBGT reduction, rainwater retention, humus and soil moisture recovery, forest evapotranspiration recovery, coastal and ocean heat-risk reduction, marine ecosystem protection, and surface-temperature reduction.

## Indexes

All values are normalized indexes from 0 to 100:

- `carbon_credit_policy_index`
- `cooling_credit_policy_index`
- `ocean_heat_load_index`
- `sea_surface_temperature_risk_index`
- `el_nino_heat_stacking_index`
- `marine_heatwave_risk_index`
- `coral_bleaching_risk_index`
- `wbgt_land_heat_risk_index`
- `food_water_stress_index`
- `urban_heat_load_index`
- `soil_moisture_recovery_index`
- `forest_evapotranspiration_recovery_index`
- `water_cycle_recovery_index`
- `ocean_circulation_support_index`
- `natural_cooling_function_index`
- `cooling_credit_intervention_index`

## Interpretation

The simulation is designed to show five conceptual points:

1. Carbon-credit-centered pathways may improve emissions accounting, but they do not directly reduce accumulated heat load.
2. El Nino risk is amplified when ocean heat load, land heat load, WBGT, soil dryness, and weak natural cooling functions overlap.
3. Cooling Credit pathways do not stop El Nino.
4. Cooling Credit pathways may reduce the severity of El Nino-related heat amplification by lowering background heat load and restoring natural cooling functions.
5. The key transition is from carbon accounting alone to thermal accounting and measurable cooling contribution.

## Outputs

- [Simulation CSV](./outputs/simulation_results.csv)
- [El Nino heat-stacking index](./outputs/el_nino_heat_stacking_index.png)
- [Carbon Credit vs Cooling Credit response](./outputs/carbon_credit_vs_cooling_credit_response.png)
- [Ocean heat-load pathways](./outputs/ocean_heat_load_pathways.png)
- [Marine heatwave risk index](./outputs/marine_heatwave_risk_index.png)
- [WBGT and land heat risk index](./outputs/wbgt_and_land_heat_risk_index.png)
- [Natural cooling recovery index](./outputs/natural_cooling_recovery_index.png)
- [Cooling Credit transition effect](./outputs/cooling_credit_transition_effect.png)
- [Causal feedback loop](./outputs/causal_feedback_loop.png)

## Run

```bash
python simulations/el_nino_heat_stacking_and_cooling_credit_transition/el_nino_heat_stacking_sim.py
```

The script writes the CSV and PNG figures into `simulations/el_nino_heat_stacking_and_cooling_credit_transition/outputs/`.

## Caution

Cooling Credits are not a license to emit. Emission reduction remains necessary. Cooling actions must be measured physically and monitored for local ecological risk. This model is a conceptual comparison tool, not a validated climate prediction system.
