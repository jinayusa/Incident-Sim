from simulator import IncidentSimulator

def main():
    print("Welcome to the Incident Response Simulation Engine")
    sim = IncidentSimulator()
    sim.load_scenarios()
    sim.run()

if __name__ == "__main__":
    main()
