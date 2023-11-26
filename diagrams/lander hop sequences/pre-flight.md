# Pre-Flight Sequence
```mermaid 
sequenceDiagram
    
    participant MCC
    participant ORB

    box LDR
        participant COM
        participant CDH
        participant SSS
        participant GNC
        participant OMS
        participant Power
        participant Mech
    end

    activate ORB
    activate CDH
    activate COM
    activate SSS
    activate Power
    activate MCC

    SSS ->> CDH: Collected sample mass threshold met
    CDH ->> COM: Sample collection complete
    COM ->> ORB: Sample collection complete
    ORB ->> MCC: Sample collection complete
    MCC ->> ORB: Move to [location]
    ORB ->> COM: Move to [location]
    COM ->> CDH: Move to [location]

    Note over CDH: Flight Preparation
        CDH ->> GNC: Generate trajectory plan to [location]
        activate GNC
        GNC -->> CDH: Trajectory plan to [location]
        deactivate GNC
        CDH ->> OMS: Heat fuel tanks
        activate OMS
        CDH ->> Power: Activate fuel cells
        Power --> CDH: Fuel cells active
        OMS --> CDH: Fuel tanks heated

        CDH ->> Mech: Enter flight configuration
        activate Mech
        Mech ->> Mech: Stow solar panels, close SCS cover
        deactivate Mech
        CDH ->> GNC: Execute trajectory plan
        activate GNC
    
    deactivate CDH
    deactivate COM
    deactivate SSS
    deactivate Power
    deactivate ORB
    deactivate MCC
    deactivate GNC
    deactivate OMS

```
