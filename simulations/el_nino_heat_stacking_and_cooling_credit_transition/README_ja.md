# エルニーニョ熱スタッキングとクーリングクレジット移行シミュレーション

このモジュールは、2015年から2035年までのエルニーニョ熱スタッキングリスクを、政策経路ごとに比較するための概念的・指数ベース・反実仮想シミュレーションである。

これは精密な気候予測ではない。蓄積した海洋熱、陸上の熱、WBGTリスク、土壌乾燥、自然冷却機能の弱体化の上にエルニーニョが重なるとき、政策フレームが何を測り、何を見落とすのかを比較するための因果モデルである。

## 中心命題

温暖化時代のエルニーニョは、単なる気象現象ではない。地球システム、とくに海洋がすでに過剰な熱を抱えていることを示す警告信号である。

カーボンクレジットが問うのは、次の問いである。

```text
どれだけCO2を削減・除去・相殺したか。
```

クーリングクレジットが問うのは、次の問いである。

```text
測定可能な冷却機能によって、どれだけ熱負荷を下げ、避け、逃がし、緩衝したか。
```

カーボンクレジットは、排出削減と会計を支える可能性がある。しかし、カーボン会計だけでは、既存の熱負荷を直接・実測的にどれだけ下げたのかを十分に示せていない。また、海洋熱、WBGT、地表温度、土壌水分、蒸散、水循環回復、海洋の冷却機能を直接評価するものでもない。

そのため、クーリングクレジットは、測定可能な冷却貢献に焦点を当てる補完的かつ移行的なフレームワークとして提案される。

## シナリオ

### A. カーボンクレジット基準線

カーボンクレジット中心の政策が継続する。排出会計は徐々に改善するが、直接的な冷却投資は弱い。自然冷却機能はゆっくり回復するか、弱体化が続く。

### B. より強い炭素緩和

CO2緩和は基準線より強く進む。しかし、直接冷却、土壌水分回復、蒸散回復、都市冷却、海洋冷却機能は不十分なままである。

### C. クーリングクレジット移行

気候資金の一部が、カーボン相殺会計から測定可能な冷却貢献へ移る。2026年以降、都市冷却、土壌水分、腐植、森林蒸散、水循環回復、海洋循環支援が増加する。

### D. クーリングクレジット加速

クーリングクレジットが主要な気候金融カテゴリーになる。都市暑熱低減、WBGT低減、雨水貯留、腐植と土壌水分回復、森林蒸散回復、沿岸・海洋熱リスク低減、海洋生態系保護、地表温度低減が、地域適応型に大規模展開される。

## 指数

すべての値は0から100の正規化指数である。

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

## 解釈

このシミュレーションは、次の5点を示すための概念モデルである。

1. カーボンクレジット中心の経路は排出会計を改善しうるが、蓄積熱負荷を直接下げるとは限らない。
2. 海洋熱、陸上熱、WBGT、土壌乾燥、弱い自然冷却機能が重なると、エルニーニョリスクは増幅される。
3. クーリングクレジットはエルニーニョを止めるものではない。
4. クーリングクレジット経路は、背景熱負荷を下げ、自然冷却機能を回復することで、エルニーニョ関連の熱増幅を弱める可能性がある。
5. 重要な移行は、カーボン会計だけから、熱会計と実測可能な冷却貢献へ移ることである。

## 出力

- [シミュレーションCSV](./outputs/simulation_results.csv)
- [エルニーニョ熱スタッキング指数](./outputs/el_nino_heat_stacking_index.png)
- [カーボンクレジットとクーリングクレジットの応答](./outputs/carbon_credit_vs_cooling_credit_response.png)
- [海洋熱負荷経路](./outputs/ocean_heat_load_pathways.png)
- [海洋熱波リスク指数](./outputs/marine_heatwave_risk_index.png)
- [WBGTと陸上暑熱リスク指数](./outputs/wbgt_and_land_heat_risk_index.png)
- [自然冷却回復指数](./outputs/natural_cooling_recovery_index.png)
- [クーリングクレジット移行効果](./outputs/cooling_credit_transition_effect.png)
- [因果フィードバックループ](./outputs/causal_feedback_loop.png)

## 実行

```bash
python simulations/el_nino_heat_stacking_and_cooling_credit_transition/el_nino_heat_stacking_sim.py
```

スクリプトはCSVとPNG図を `simulations/el_nino_heat_stacking_and_cooling_credit_transition/outputs/` に出力する。

## 注意

クーリングクレジットは排出の免罪符ではない。排出削減は引き続き必要である。冷却行為は物理的に測定され、地域生態リスクも監視されなければならない。このモデルは概念比較ツールであり、検証済みの気候予測システムではない。
