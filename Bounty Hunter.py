from time import sleep
from random import randint
from math import hypot
from os import system
#from winsound import Beep

def ConfigureCmd():
    system("echo off")
    system("color 0a")
    system("cls")

ConfigureCmd()

#Agents&Target setup
AgentSmith = [randint(1, 100), randint(1, 100)]
Agent1 = [randint(1, 100), randint(1, 100)]
Agent2 = [randint(1, 100), randint(1, 100)]
Agent3 = [randint(1, 100), randint(1, 100)]
Agent4 = [randint(1, 100), randint(1, 100)]
Target = [randint(1, 100), randint(1, 100)]

def transmit(subject1: list, subject2: list) -> None:
    sleep(hypot(abs(subject1[0]-subject2[0]), abs(subject1[1]-subject2[1]))/10)

def Setup():
    print(f"Intel is searching the Target{Target}")
    sleep(randint(2, 5))
    print()
    print(f"Intel found the Target{Target}")
    sleep(2)
    print()
    print(f"Intel is now transmitting the location of the Target{Target} to AgentSmith{AgentSmith}")
    sleep(randint(1, 5))
    print()
    print(f"AgentSmith{AgentSmith} received the location of the Target{Target}")
    sleep(2)
    print()
    print(f"AgentSmith{AgentSmith} is now Transmitting the location of the Target{Target} to Agent1{Agent1}")
    transmit(AgentSmith, Agent1)
    print()
    print(f"AgentSmith{AgentSmith} is now Transmitting the location of the Target{Target} to Agent2{Agent2}")
    transmit(AgentSmith, Agent2)
    print()
    print(f"AgentSmith{AgentSmith} is now Transmitting the location of the Target{Target} to Agent3{Agent3}")
    transmit(AgentSmith, Agent3)
    print()
    print(f"AgentSmith{AgentSmith} is now Transmitting the location of the Target{Target} to Agent4{Agent4}")
    transmit(AgentSmith, Agent4)
    print()
    print("All Agents Are Good To Go")

def Hunt():
    print()
    print("Agents started the Hunt")
    print()
    while True:
        print(f"AgentSmith: {AgentSmith}")
        print(f"Agent1    : {Agent1}")
        print(f"Agent2    : {Agent2}")
        print(f"Agent3    : {Agent3}")
        print(f"Agent4    : {Agent4}")
        print(f"Target    : {Target}")
        print()
        if AgentSmith == Target:
            print(f"AgentSmith({AgentSmith[0]}, {AgentSmith[1]}) got the Target({Target[0]}, {Target[1]})")
            break
        elif Agent1 == Target:
            print(f"Agent1({Agent1[0]}, {Agent1[1]}) got the Target({Target[0]}, {Target[1]})")
            break
        elif Agent2 == Target:
            print(f"Agent2({Agent2[0]}, {Agent2[1]}) got the Target({Target[0]}, {Target[1]})")
            break
        elif Agent3 == Target:
            print(f"Agent3({Agent3[0]}, {Agent3[1]}) got the Target({Target[0]}, {Target[1]})")
            break
        elif Agent4 == Target:
            print(f"Agent4({Agent4[0]}, {Agent4[1]}) got the Target({Target[0]}, {Target[1]})")
            break
        else:
            for i in range(0, 2):
                if AgentSmith[0] < Target[0]:
                    AgentSmith[0] += 1
                if AgentSmith[0] > Target[0]:
                    AgentSmith[0] -= 1
                if AgentSmith[1] < Target[1]:
                    AgentSmith[1] += 1
                if AgentSmith[1] > Target[1]:
                    AgentSmith[1] -= 1

            if Agent1[0] < Target[0]:
                Agent1[0] += 1
            if Agent1[0] > Target[0]:
                Agent1[0] -= 1
            if Agent1[1] < Target[1]:
                Agent1[1] += 1
            if Agent1[1] > Target[1]:
                Agent1[1] -= 1

            if Agent2[0] < Target[0]:
                Agent2[0] += 1
            if Agent2[0] > Target[0]:
                Agent2[0] -= 1
            if Agent2[1] < Target[1]:
                Agent2[1] += 1
            if Agent2[1] > Target[1]:
                Agent2[1] -= 1

            if Agent3[0] < Target[0]:
                Agent3[0] += 1
            if Agent3[0] > Target[0]:
                Agent3[0] -= 1
            if Agent3[1] < Target[1]:
                Agent3[1] += 1
            if Agent3[1] > Target[1]:
                Agent3[1] -= 1

            if Agent4[0] < Target[0]:
                Agent4[0] += 1
            if Agent4[0] > Target[0]:
                Agent4[0] -= 1
            if Agent4[1] < Target[1]:
                Agent4[1] += 1
            if Agent4[1] > Target[1]:
                Agent4[1] -= 1
            
            if randint(0, 1000) == randint(0, 1000):
                print(f"Target Jumped")
                print()
        sleep(1)
    #Beep(1000, 1000)

Setup()
Hunt()
