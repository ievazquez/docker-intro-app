go mod graph | sed -Ee 's/@[^[:blank:]]+//g' | sort | uniq >unver.txt

##Graph

digraph {
graph [overlap=false, size=14];
root="$(go list -m)";
node [ shape = plaintext, fontname = "Helvetica",
fontsize=24];
"$(go list -m)" [style = filled,
fillcolor = "#E94762"];

apt-get install graphviz


sfdp -Tsvg -o graph.svg graph.dot