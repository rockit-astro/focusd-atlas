## FLI Atlas Focuser daemon

`focusd` interfaces with and wraps a FLI Atlas focuser and exposes it via Pyro.

`focus` is a commandline utility for controlling the focuser.

### Configuration

Configuration is read from json files that are installed by default to `/etc/focusd`.
A configuration file is specified when launching the server, and the `focus` frontend will search this location when launched.

The configuration options are:
```python
{
  "daemon": "warwick_focuser", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "focusd@warwick", # The name to use when writing messages to the observatory log.
  "control_machines": ["WarwickTCS"], # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `rockit.common.IP`.
  "move_timeout": 20, # Maximum time to move between any two positions
}

```
## Initial Installation

The automated packaging scripts will push 4 RPM packages to the observatory package repository:

| Package                   | Description                                                                  |
|---------------------------|------------------------------------------------------------------------------|
| rockit-atlas-server       | Contains the `focusd` server and systemd service file.                       |
| rockit-atlas-client       | Contains the `focus` commandline utility for controlling the focuser server. |
| python3-rockit-atlas      | Contains the python module with shared code.                                 |
| rockit-atlas-data-warwick | Contains the json configuration for the Windmill Hill Observatory telescope. |

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now focusd@<config>
```

where `config` is the name of the json file for the appropriate telescope.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart focusd@<config>
```

### Testing Locally

The camera server and client can be run directly from a git clone:
```
./focusd test.json
FOCUSD_CONFIG_PATH=./warwick.json ./focus status
```
