start with a 2D box. Place a source point random in the box. Place a set of destinations randomly in the box.
--> Find the shortest number of links connecting all points from the distribution
* place a set of links
* sum the distance of each links

   1) naive implementation: direct connection from the source to each destination
   2) connect directly from source to nearby destinations. Connect from each of those destinations
   3) introduce a set of intermediate distribution points
   
