The following details were used to develop the scripts.

  1. Config file contains the starting and ending co-ordinates of all the objects. Make sure that the parcel is placed on the chasis ( trial and error ).
  2. Develop an Odometric model wherein the next state can be estimated. This was primaraly done use FK and INK methods. 
  3. An dedicated script was developed to plan the path of the end-effector. A fixed screw trajectory generation was tested.
  4. ANFIS based methods for trajectory generation was also tested but it did not give good results and was very unstable.
  5. Feedforward Control scheme was designed.
  6. Finally, the Jacobian was used to find all the speeds and configuration required.
