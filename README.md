# Simple python script which queries the traffic counter of Deutsche Telekom

## Installation
You need Python >= 3.7 and virtual env to run this.

## Usage
Calling this scrpt on a device connected to the internet via a cellphone network
of Deutsche Telekom (or a reseller of Deutsche Telekom), the script
will output the traffic used as well as the traffic included:

```
> python3 datapass.py
Datennutzung: 
	Tarif: Dein Datenvolumen
	Datenvolumen: 1,5 GB
	Verbraucht: 861,28 kB (1%)
```

## References

### Source Code
Can be found on [GitHub](https://github.com/kettenbach-it/deutsche-telekom-datapass-traffic-counter-query)

## License
GNU AGPL v3

Fore more, see [LICENSE](LICENSE)
