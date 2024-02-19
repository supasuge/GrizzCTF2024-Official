# Probability Ability


#### Build/Deployment
1. cd into the correct directory
`cd Probability_Ability/src`
2. Build the correct image
`docker build -t probability-ability .`
3. Deploy the image
`docker run -dit -p 9999:9999 --name probability-ability probability-ability:latest`