# 🦟 Dengue Spread Model (NetLogo)

## Overview

This is an **agent-based simulation** of **dengue virus transmission** between *humans*, *mosquitoes*, and *larvae* in a simplified environment. The model emphasizes **realistic dynamics**, with **1 tick = 1 day**, and includes factors like multiple dengue serotypes, secondary infections, mosquito reproductive cycles, and mortality rates influenced by healthcare access.

## 📁 Contents

- `setup` – Initializes the model world
- `go` – Main simulation loop (1 day per tick)
- Agents:
  - `humans` – Individuals who can get infected and recover or die
  - `mosquitoes` – Disease vectors; can be infected and reproduce
  - `larvae` – Mosquito offspring that may hatch or die before maturing
- Environment:
  - `water` patches used for mosquito reproduction

## 🧪 Purpose

This model helps study:

- Transmission dynamics of **dengue virus**
- Effects of **healthcare access** on mortality
- Interactions between **human and mosquito populations**
- Impact of **serotype diversity** on infection severity

## 🧬 Key Features

### ➕ Multi-Serotype Dengue Infections

- Mosquitoes and humans can carry/infect with **DENV-1** to **DENV-4**
- Humans track which serotypes they’ve had (`dengue-serotypes`)
- Secondary infections cause **severe dengue**, with increased mortality risk

### 💉 Healthcare Access

- 80% of humans have access to care (`has-care?`)
- Access reduces fatality risk for severe dengue

### 🧍 Human Behavior

- Move randomly
- Recover or die based on infection severity and healthcare access
- Infection tracked by color:
  - Green: healthy
  - Red: initially infected
  - Yellow: severe/secondary infection

### 🦟 Mosquito Lifecycle

- Females bite every **3 days** after maturity
- May infect or acquire dengue from humans
- Lay eggs in **nearby water patches**
- Hatch into mosquitoes after 5–9 days (if they survive)

### 🐛 Larvae

- Have a **chance of dying** before maturing (30%–90%)
- Track death toll and hatching success

## 🔢 Parameters (Define in Interface)

Make sure you define these **global parameters** in the Interface tab (as sliders or input boxes):

- `init-total-humans` (e.g., 100)
- `init-total-mosquitoes` (e.g., 200)
- `init-n-human-infected` (e.g., 5)
- `water-density` (percentage, e.g., 10)

## 📊 Monitors (Optional)

You can add Interface elements to track:

- `%infected-humans`
- `%infected-mosquitoes`
- `%recovered-humans`
- `human-death-toll`
- `mosquito-death-toll`
- `larvae-death-toll`
- `n-human-infected`
- `n-mosquito-infected`

## 🧭 Usage

1. **Set parameters** in the Interface tab.
2. Click **Setup** to initialize agents and environment.
3. Click **Go** to run the simulation tick-by-tick (1 tick = 1 day).
4. Observe how infections spread, recoveries occur, and how mosquito populations affect human health.

## 📌 Notes

- Mosquito reproduction only happens **near water patches**.
- Only **female mosquitoes** bite and lay eggs.
- Larvae survival and mosquito lifespan are stochastic (randomized).
- `custom-chance-larvae?` is declared but not yet implemented in full logic.

## 🔧 Suggested Improvements

- Enable toggling `custom-chance-larvae?`
- Add GUI controls for climate/seasonality
- Introduce vaccination or vector control interventions
- Include spatial barriers or human clustering

## 📚 References

This model is based on general principles of dengue epidemiology, including:
- WHO dengue factsheets
- Vector-borne disease modeling literature
- Agent-based modeling principles (e.g., NetLogo framework)

## 🧠 Author & Credits

Created using **NetLogo** for simulation and research purposes.

Feel free to modify, extend, or use in educational settings with proper attribution.
