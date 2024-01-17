# Mission Timeline
```mermaid

gantt
    dateFormat YYYY-MM-DD
    section Transit to Enceladus 
        Launch :milestone, launch, 2033-09-14, 0d
        LEOP: 7d
        Transit to Venus :8952h
        Venus Gravity Assist :milestone,
        Transit to Earth :9384h
        Earth Gravity Assist :milestone,
        Transit to Venus:1104h
        Venus Gravity Assist :milestone,
        Transit to Earth :20136h
        Earth Gravity Assist :milestone,
        Transit to Saturn:34992h
        Saturn Orbit Insertion :milestone,
        <!-- Moon Tour:30672h -->
        Enceladus Orbit Insertion :milestone,
```

```mermaid

gantt
    dateFormat YYYY-MM-DD
    section Enceladus Operations
        Enceladus Orbit Insertion :milestone, (unknown date),
        Reconnaissance :504h
        Lander Deployment :milestone,
        Sample collection & traversal: 1792h
        Lander Rendevouz: milestone,
```

```mermaid

gantt
    dateFormat YYYY-MM-DD
    section Return Journey
        Lander Rendevouz: milestone, 2045-12-27,
        Transit to Earth:61323.5h
        Earth orbit injection & return capsule deployment: milestone,

```