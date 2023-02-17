set terminal png enhanced 


set datafile separator ";"
set key above right 

set title "Clusterization 1002 points (10 iterations)" #titulo

set output "graph0.png"

plot "arquivo0" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo0" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

set title "Clusterization 2004 points (10 iterations)" #titulo

set output "graph1.png"

plot "arquivo1" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo1" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

set title "Clusterization 3006 points (10 iterations)" #titulo

set output "graph2.png"

plot "arquivo2" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo2" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

set title "Clusterization 4008 points (10 iterations)" #titulo

set output "graph3.png"

plot "arquivo3" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo3" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

set title "Clusterization 4008 points (10 iterations)" #titulo

set output "graph4.png"

plot "arquivo4" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo4" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

set title "Clusterization 6012 points (10 iterations)" #titulo

set output "graph5.png"

plot "arquivo5" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo5" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

set title "Clusterization 4008 points (10 iterations)" #titulo

set output "graph6.png"

plot "arquivo6" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo6" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

set title "Clusterization 4008 points (10 iterations)" #titulo

set output "graph7.png"

plot "arquivo7" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo7" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 


set title "Clusterization 4008 points (10 iterations)" #titulo

set output "graph8.png"

plot "arquivo8" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo8" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 


set title "Clusterization 4008 points (10 iterations)" #titulo

set output "graph9.png"

plot "arquivo9" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo9" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

set title "Clusterization 4008 points (10 iterations)" #titulo

set output "graph10.png"

plot "arquivo10" using ($3 == 1? x=$1 : 1/0) : ($3 == 1? y=$2 : 1/0) title "Pontos" with points pt 7 ps 0.5 , \
    "arquivo10" using  ($3 == 0? x=$1 : 1/0) : ($3 == 0? y=$2 : 1/0) title "Centro" with points pt 9 ps 2 

