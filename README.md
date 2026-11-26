# retire-mount

This project uses retire to crawl a mount or a folder for outdated js files, and any linked files on other servers and drops them in json files for your analysis.


## Getting Started

### Dependencies

* docker; this way, we're not bogged down by unforseen os differences

### Installing

* Create a .env file with DIR="your folder to crawl" (relative to local path, absolute is best)
(.env.example exists to be copied, if you prefer)

### Executing program

* run docker compose up (it should exit with code 0 after a little while)
* look into your output folder for the json files. If both are empty, you're good :)

## Authors

Contributors names and contact info

ashnack

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the GNU Lesser General Public License.
