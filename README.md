# Hockey Gatekeeper Index 🏒

A spatial analytics engine designed to quantify defensive transition effectiveness and "Gap Control" using IIHF Olympic player-tracking data.

## 📌 Project Overview
In modern hockey, the ability to "kill" plays at the blue line is a premier defensive skill. While traditional box scores track hits or blocked shots, they fail to capture **Gap Control**—the physical distance a defender maintains against an attacking puck carrier.

The **Gatekeeper Index** automates this scouting process by:
1.  **Detecting Transitions:** Identifying the exact frame the puck crosses the blue line into the defensive zone.
2.  **Measuring the Gap:** Calculating the Euclidean distance between the puck carrier and the primary defender at the moment of entry.
3.  **Ranking Performance:** Aggregating data across multiple games to identify which defenders consistently suppress space.

## 🛠️ Tech Stack
* **Language:** Python 3.12.10
* **Data Handling:** Pandas, NumPy
* **Geometry:** Euclidean Distance Modeling
* **Environment:** Virtual Environments (venv)

## 📂 Repository Structure
* `src/loader.py`: Handles data ingestion and roster synchronization.
* `src/entry_detector.py`: Logic for detecting blue line crossings with a 60-frame "debounce" cooldown.
* `src/gap_analyzer.py`: Spatial logic to identify the closest defender and calculate gap distance.
* `src/gatekeeper_score.py`: Aggregation engine to produce player leaderboards.
* `main.py`: The central execution pipeline.

## 📊 Sample Insights (Full Game Batch)
Using 2022 Olympic tracking data across multiple Power Play segments, the engine analyzed **37 unique zone entries**.

**Defensive Performance Leaderboard:**
| Player | Entries Faced | Avg Gap (ft) | Min Gap (ft) |
| :--- | :--- | :--- | :--- |
| Dani Cameranesi | 1 | 5.29 | 5.29 |
| Ashton Bell | 2 | 12.58 | 8.17 |
| Jocelyne Larocque | 3 | 18.72 | 7.25 |
| Brianne Jenner | 4 | 22.09 | 10.06 |

*Insight: Brianne Jenner emerged as the most frequent 'Gatekeeper' in the sample, while Dani Cameranesi recorded the tightest single gap at 5.29 feet.*

## 🚀 Getting Started
1. Clone the repo: `git clone https://github.com/anthonydevito/hockey-gatekeeper-index.git`
2. Create venv: `python -m venv venv`
3. Activate venv: `.\venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install pandas numpy`
5. Run the engine: `python main.py`
