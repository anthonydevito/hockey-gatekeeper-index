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

## 📊 Sample Insights
Using 2022 Olympic tracking data, the engine successfully identified elite defensive stands. 

**Top "Gatekeepers" (Lowest Avg Gap):**
| Player | Entries Faced | Avg Gap (ft) | Min Gap (ft) |
| :--- | :--- | :--- | :--- |
| Jocelyne Larocque | 1 | 7.25 | 7.25 |
| Ashton Bell | 1 | 8.17 | 8.17 |
| Erin Ambrose | 1 | 10.02 | 10.02 |

*Note: Smaller gap distances indicate tighter defensive coverage and higher play-suppression probability.*

## 🚀 Getting Started
1. Clone the repo: `git clone https://github.com/anthonydevito/hockey-gatekeeper-index.git`
2. Create venv: `python -m venv venv`
3. Activate venv: `.\venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install pandas numpy`
5. Run the engine: `python main.py`