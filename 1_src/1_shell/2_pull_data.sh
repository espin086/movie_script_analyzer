if [ $1 = "--h" ]
then
	echo ""
    echo "************** HELP FILE **************"
    echo ""
    echo "Author: JJ Espinoza"
    echo "Description: Scrapes data from the web"
    echo ""
    echo "---------------------------------------"
    echo ""
    echo "Commands:                               Info:"
    echo "./2_pull_data.sh --h		        Help Menu"
    echo "./2_pull_data.sh --releases	Pulls data for future film releases"
    echo ""
    echo "Current Directory is: "
    pwd
    echo ""
    echo "---------------------------------------"

fi

if [ $1 = "--releases" ]
then
Rscript /Users/jje/Documents/00__mytools/3_mojo/1_src/2_r/1_future_release_dates.R
fi
