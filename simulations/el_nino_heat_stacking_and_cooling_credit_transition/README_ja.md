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
- `accumulated_ocean_heat_index`
- `heat_inertia_index`
- `climate_time_lag_index`
- `existing_heat_load_index`
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
- `direct_cooling_intervention_index`
- `natural_cooling_recovery_index`
- `thermal_accounting_index`

## 解釈

このシミュレーションは、次の5点を示すための概念モデルである。

1. カーボンクレジット中心の経路は排出会計を改善しうるが、蓄積熱負荷を直接下げるとは限らない。
2. 海洋熱、陸上熱、WBGT、土壌乾燥、弱い自然冷却機能が重なると、エルニーニョリスクは増幅される。
3. クーリングクレジットはエルニーニョを止めるものではない。
4. クーリングクレジット経路は、背景熱負荷を下げ、自然冷却機能を回復することで、エルニーニョ関連の熱増幅を弱める可能性がある。
5. 重要な移行は、カーボン会計だけから、熱会計と実測可能な冷却貢献へ移ることである。

## 熱慣性と費用対効果の解釈

熱慣性の問題こそ、カーボン会計だけでは不十分である最大の理由である。気候システムに蓄積された余剰熱の90%以上は海洋に吸収されているため、気候問題は、蓄積熱、時間差、自然冷却機能の弱体化の問題でもある。

排出削減はブレーキである。追加的な熱の流入を防ぐ助けになるが、海洋、陸地、都市環境、土壌、大気中の水蒸気システムにすでに蓄積された熱を即座に取り除くものではない。

そのため、このシミュレーションは次の3層を区別する。

```text
1. 追加的な熱の流入を防ぐこと
2. 既存の熱負荷を下げ、または緩衝すること
3. 自然冷却機能を回復すること
```

カーボン会計が主に扱うのは第一層である。クーリングクレジットは第二層と第三層を扱うために提案される。

カーボンクレジット中心の経路では、会計スコアが改善しても、物理的な熱負荷指標が高いまま残る可能性がある。クーリングクレジット経路は、次の指標を直接下げ、または緩衝できるかで評価されるべきである。

- 海洋熱負荷指数
- 海洋蓄熱指数
- 熱慣性・気候タイムラグ指数
- WBGTリスク
- 地表・都市熱
- 土壌乾燥
- 水循環不全
- 自然冷却機能の低下
- エルニーニョ熱スタッキング増幅

これは費用対効果の問題でもある。カーボンクレジットとカーボンプライシングは、排出量会計、規制対応、一定の緩和資金として機能しうる。しかし、会計が改善しても蓄積熱負荷の実測可能な冷却につながらないなら、カーボンクレジット中心の制度は主要な気候資金メカニズムとして十分な費用対効果を示していない。

地球は、排出量が会計上相殺されたから冷えるのではない。熱の流入を減らし、すでに存在する熱負荷を物理的に下げ、緩衝し、自然冷却機能を回復したときにだけ冷える。

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

---

## 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
自然法則思想、地球循環再生、AIとの共創を中心に公開活動を行う。

---

## ライセンス

CC BY 4.0

本記事は、Creative Commons Attribution 4.0 International License（CC BY 4.0）で公開する。  
著者表示を行う限り、共有、転載、翻訳、改変、再利用を許可する。
