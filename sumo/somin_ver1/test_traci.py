import traci
import os
import time

# SUMO 실행 명령어
sumo_binary = "sumo"  # or "sumo-gui" if you want GUI
sumocfg_file = "RL_routest.sumocfg"  # sumocfg 경로


def run_simulation():
    traci.start([sumo_binary, "-c", sumocfg_file])

    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        # 예시: 교차로의 신호등 상태를 가져오기
        tls_id = traci.trafficlight.getIDList()[0]  # 첫 번째 신호등
        current_phase = traci.trafficlight.getRedYellowGreenState(tls_id)
        print(f"Step {step}: Traffic Light = {current_phase}")

        # 예시: 차량 상태
        for veh_id in traci.vehicle.getIDList():
            speed = traci.vehicle.getSpeed(veh_id)
            pos = traci.vehicle.getPosition(veh_id)
            print(f"  Vehicle {veh_id} | Speed: {speed:.2f} | Pos: {pos}")

        step += 1
        time.sleep(0.2)
    traci.close()
    print("Simulation finished.")


if __name__ == "__main__":
    run_simulation()
