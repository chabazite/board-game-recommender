# board-game-recommender
An App that serves a board game recommender algorithm

**Link to Webapp**: **<a href="https://dnd-monsters-df92bbf34eb8.herokuapp.com/" target="_blank">DnD Monster Generator</a>**
==============================
DnD_Monsters
==============================

## Business Case
<a name="Business_Case"></a>
In 1974, Dungeons and Dragons was created by designers Gary Gygax and David Arneson. While I wasn’t alive, I can certainly guarantee some of the same problems that are discussed in the realm of DnD today, were discussed around the tables then as well. One of these issues is the Dungeon Master’s (DM) struggle to create a perfectly balanced encounter. 

This issue has certainly come a long way. In the 1st and 2nd editions, DMs had to decide just based on the stats of the monster as well as the experience, if these monsters could put up an adequate fight for the party level in question. In the 3rd edition, we received something known as the Challenge Rating (CR) and Encounter Levels (EL). In 4th edition, we moved into Encounter Levels and daily experience budgets. In 5e, Wizards of the Coast took us back to Challenge Ratings, but this time with a much more streamlined system.

All of this however assumes that the Dungeon Master only uses the 2,460 monsters that have been created throughout the 5e sourcebooks. While that looks like quite a bit of monsters, an inexperienced DM may not have access to all the books, and even further, those monsters span 20 player levels. If we are a brand new DM, we may only have access to around 300 monsters from the System Reference Document (SRD). Over 20 levels, that isn’t much to choose from after your first campaign. With a game that has always been about the freedom, exploration, and creativity of its players, you can almost guarantee DMs will want to create their own monstrosities. 

Luckly, Wizards of the Coast has always known this. Even in 3.5e, they provided a way for Dungeons Masters to become their own Dr. Frankensteins! This system has since been streamlined and in 5e Wizards of the Coast brought us a Challenge Rating equation. A simple way to use hit points, armor class, attack bonus, and attack damage per round to start molding your own monster for whatever level you choose. Unfortunately, this process still takes a bit of effort, doesn’t include many of the nuances that make monsters so scary, and finally many DMs have even said it doesn’t provide the results they hoped for. 

To be honest, I don’t know that we will ever get to a place that is both simple and all-encompassing for monster creation. That’s because balancing an encounter falls onto the DM experience, and a lot of it isn’t even monster related: 
  * What kind of resources do the players have left for the day? 
  * Are there any environmental hazards in this fight? 
  * Is there a secondary or primary goal other than ‘kill the monster’ that the party will focus on? 
  * Is there a single monster, a boss with minions, or several semi-boss level characters to worry about?
  * Not to mention…the rolls, one good or bad roll on either side could mean a huge swing in the favor of the monster or the players.

These questions and others will sway the battle difficulty without even considering the level of the monster. This is why encounter building is considered such a nuanced art for DMs.
Like I said, I don’t know that it will ever be possible to create the perfect system for choosing monsters for players. There is so much variance just from table to table, that I believe you would have to restrict the game a considerable amount in order for something consistent to appear. And that certainly is not in the spirit of Dungeons and Dragons.
With all that being said, I am still curious if there is an easier way for Dungeon Masters to create a monster stat block on the fly. One that may be more in line with the monsters from the manual. While it may not be perfect, it will eventually allow us to create something very quickly that we can then spend time tweaking and turning into a beautiful encounter. Rather than spending the time trying to create the monster itself.


To that end, this project focused on three major questions:
1. How different is the Challenge Rating when used to calculate the CR of Monster Manual Monsters?
2. How does the monster’s non-stat oriented categories (type, environment, size, alignment) impact its stats?
3. Can we predict a monster stat block for inexperienced DMs that resembles SRC monsters?

Check out my medium post <a href="https://medium.com/@Andrew-Ingalls/using-tensorflow-to-build-a-balanced-dnd-monster-generator-c942f4456626">here</a>

## Table of Contents
<details open>
  <summary>Show/Hide</summary>
  <br>
 
1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Structure ](#Structure)
4. [ Evaluation ](#Evaluation)
5. [ Future Improvements ](#Future_Improvements)

</details>


## Project Organization

<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
 <br>

--------
  </details>   

## Technologies Used:
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>

 
 ------------
 </details>

## Structure of Notebooks:
<details>
<a name="Structure"></a>
<summary>Show/Hide</summary>
<br>


1. Backend:
    - Framework: 
        - FastAPI - Easy tensorflow integration and RESTful API
        - Flask -  user authentication, databaase access, website routing. 
    - Recomendation Engine: TensorFlow
2. Database:
    - PostgreSQL
3. Front-End:
    - HTML/CSS/JavaScript
4. Hosting:
    - Heroku

 </details>

## Evaluation:
<a name="Evaluation"></a>
<details>
<summary>Show/Hide</summary>
<br>

</details>
  
## Future Improvements
 <a name="Future_Improvements"></a>
 <details>
<summary>Show/Hide</summary>
<br>

</details>

<p><small>Project structure based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
<p><small>CI/CD Deployment Resource for Heroku: <a target="_blank" href="https://towardsdatascience.com/deploy-containerized-plotly-dash-app-to-heroku-with-ci-cd-f82ca833375c">Heroku Deployment Resouce</a></small></p>
<p>README outline tailored from [awesomeahi95][]<p>
