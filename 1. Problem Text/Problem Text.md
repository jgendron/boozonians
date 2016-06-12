# Alien-nation Hackathon

## Problem Statement
You have just arrived in orbit of an alien world called Hamiltus with abundant signs of life as part of the first manned mission to the planet.  The planet is inhabited by a humanoid alien race known as Boozonians.

Previous unmanned probes sent to the planet have discovered that many of the Boozonians are young peace loving urban dwellers who are friendly and drink craft beer on the planet's equivalent of U Street or Adams Morgan.

However, these same probes also indicated that many other Boozonians are slightly older ex-military officers and intelligence analysts who were alive to see the original Independence Day movie in 1996.  They are likely to be hostile to a perceived alien invasion.

Before you and the rest of the crew descend to the surface in 3 hours, it is important to know what you will encounter. As the Data Science Officer aboard the ship, your mission is to analyze data collected by several probes previously sent to the planet to try to differentiate between friendly and hostile lifeforms.

Once you have built a model it will be uploaded to every astronaut's onboard spacesuit computer to instantly analyze a Boozonian as friendly or hostile.  The team is counting on you to make it down and back alive. Good luck!

## Background Information

This data set provides information about probe samples of various species of planet Hamiltus lifeforms called Boozonians.  Each species is  identified as either friendly or dangerous based on extensive lab testing and machine learning predictions of probe results.

## Background Information

This data set provides information about probe samples of various species of planet Hamiltus lifeforms called Boozonians.  Each species is  identified as either friendly or dangerous based on extensive lab testing and machine learning predictions of probe results.

## Data Description
1. Relevant Information:
    
2. Number of Instances: 8,123

3. Number of Attributes: 21 (all nominally valued)

4. Attribute Information: (classes: edible=e, poisonous=p)
     1. head-shape:                bell=b,conical=c,convex=x,flat=f,
                                  knobbed=k,sunken=s
     2. head-surface:              fibrous=f,grooves=g,scaly=y,smooth=s
     3. head-color:                brown=n,buff=b,cinnamon=c,gray=g,green=r,
                                  pink=p,purple=u,red=e,white=w,yellow=y
     4. lesions:                  lesions=t,no=f
     5. odor:                     almond=a,lemon=l,creosote=c,fishy=y,foul=f,
                                  musty=m,none=n,pungent=p,spicy=s
     6. gill-attachment:          attached=a,descending=d,free=f,notched=n
     7. gill-spacing:             close=c,crowded=w,distant=d
     8. gill-size:                broad=b,narrow=n
     9. gill-color:               black=k,brown=n,buff=b,chocolate=h,gray=g,
                                  green=r,orange=o,pink=p,purple=u,red=e,
                                  white=w,yellow=y
    10. body-shape:              enlarging=e,tapering=t
    11. body-shape-surface-above-neck: fibrous=f,scaly=y,silky=k,smooth=s
    12. body-surface-below-neck:  fibrous=f,scaly=y,silky=k,smooth=s
    13. body-shape-color-above-neck:   brown=n,buff=b,cinnamon=c,gray=g,orange=o,
                                  pink=p,red=e,white=w,yellow=y
    14. body-color-below-neck:    brown=n,buff=b,cinnamon=c,gray=g,orange=o,
                                  pink=p,red=e,white=w,yellow=y
    15. foot-type:                partial=p,unknown=u
    16. foot-color:               brown=n,orange=o,white=w,yellow=y
    17. number-heads:             none=n,one=o,two=t
    18. eye-type:                cobwebby=c,evanescent=e,flaring=f,large=l,
                                  none=n,pendant=p,sheathing=s,zone=z
    19. tattoo-print-color:       black=k,brown=n,buff=b,chocolate=h,green=r,
                                  orange=o,purple=u,white=w,yellow=y
    20. population:               abundant=a,clustered=c,numerous=n,
                                  scattered=s,several=v,solitary=y
    21. habitat:                  gas-mines=g,lower-regions=l,mid-planet=m,plateaus=p,
                                  underground=u,water-based=w,developed-cities=d

5. Class Distribution: 
    --  friendly: 4208 (51.8%)
    -- dangerous: 3915 (48.2%)
    --     total: 8123 instances

## Submission Format
Provide your predictions in a __plain text__ file with one prediction per line __without__ a header line or row numbers. Use only the words `dangerous` and `friendly` to indicate your predictions. Save the file as <team_name>.txt.  The file will look something like this:

friendly  
dangerous  
friendly  
friendly  
friendly  
dangerous  
friendly  
friendly  
...  


Good luck and happy predicting.
