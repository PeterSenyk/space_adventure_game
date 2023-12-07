# term_project_sud

Every program needs a README.md

## Your name:

Peter Senyk

## Your student number:

A01376857

## Your GitHub username:

PeterSenyk

## Any important comments you'd like to make about your work:

REPLACE THIS LINE WITH ANY COMMENTS


TUTORIAL

SHIPS:
    *** For testing purposes, selecting "Z" during any ship selection screen will return a test ship that makes gameplay easy
    when given the opportunity to choose new ships the stats are represented as
    ATTACK: The amount of damage a ship can do per attack
    MOVEMENT: The speed/agility of the ship
    SHIELD: Absorbs attack damage point for point, shields also regenerate
    HP: The hull health of your ship, if this reaches zero its game over
    TARGETING: A higher targeting stat means a higher chance for your attack to land
    CARGO: Holds found gear or cargo to transport

ACTIONS:
    MOVE: Select a direction for your character to move their ship within the space grid
    SCAN: Send a radar ping, displaying all tiles in your space grid
    Personal Stats: Display your character Title and Name, along with current HP and SHIELD values for your ship

======EVENTS=======

COMBAT:
    ATTACK: Start an attack sequence with the hostile ship
            Order is determined by both ships movement value, higher speed and agility means you go first
            Chance to hit is determined by TARGETING value of the attacker, and MOVEMENT value of the defender
                If an attack misses, the defenders SHIELDS recharge by one point
            Damage is dealt to SHIELDS first, if SHIELDS have zero points, the remaining attack points are dealt to HP
            If a ships HP is zero or below, the ship has exploded and the combat is over
    DODGE: You do not attempt to attack the hostile ship
            Instead the chance for the hostile ships attack to miss increases, giving you a chance to recharge your SHIELDS
    RUN: You escape the fight, if your ship MOVEMENT is not high enough you will take damage while escaping
    SCAN: Display your ships current stats, as well as the hostile ship stats

DEBRIS:
    You're given possible routes to avoid the debris in space
    CORRECT GUESS: You slip past the debris, allowing your SHIELD to recharge one point
    INCORRECT GUESS: You fly into the space debris taking one damage, hopefully you have SHIELDS

ASTEROID BELT:
    Very similar to debris in space, but there's a chance of having to avoid more than one collision
    CORRECT GUESS: You slip past the debris, allowing your SHIELD to recharge one point
    INCORRECT GUESS: You fly into the space debris taking one damage, hopefully you have SHIELDS

SHIP WRECK: 
    There's a chance you find spare parts, upgrading your ship, or repairing some hull damage (+1 HP)
    There's also a chance that you instead meet the hostile ship that caused the wreckage, starting COMBAT

MOON:
    There's a chance of hostile ships waiting for you here, starting COMBAT
    If there's no hostile ship, listen to some Pink Floyd, and let your SHIELD recharge by one point


======MISSIONS=====

LEVEL ONE: Complete space combat and dodge debris, get one point for doing either successfully, You need a combined value of 4 to complete the first level

LEVEL TWO: Avoid the hazards of space while you track down the pirate that stole some tech from Arc-Corp, defeat the pirate and return the cargo to the station to 
            complete level two

LEVEL THREE: Explore deep into space to investigate a spacial anomaly that appeared on the radar, 






