# Vaccine IoT Monitoring System


## Project Hierarchy


```
.
├── containers
│   ├── docker-compose.yml
│   ├── mosquitto
│   │   ├── config
│   │   ├── data
│   │   └── log
│   ├── mqtt_docker_run_old.sh
│   ├── mqtt_trail_subscribe.py
│   └── volumes
│       └── data01
├── LICENSE
├── README.md
└── src
    ├── host_scripts
    │   ├── mqtt_to_elastic.py
    │   └── sensor_to_elastic_old.py
    └── pi_scripts
        ├── adafruit_libs
        ├── BH1750_i2c.py
        ├── BMP180_i2c
        ├── bmp180_usinglib.py
        ├── BMP280_i2c.py
        ├── DHT11.py
        ├── minor
        ├── pi_to_elastic_direct_old.py
        └── pi_to_mqtt.py
```

### Important Notes

Elastic container requires high vm memory, so need may rise to run this command

```bash
sudo sysctl -w vm.max_map_count=262144
```
