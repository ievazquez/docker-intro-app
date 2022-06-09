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


###

git clone https://github.com/mlabouardy/recipes-api.git
cd recipes-api
touch README.md
git checkout -b preprod
git push origin preprod
git checkout –b develop
git push origin develop

## Create

curl --location --request POST 'http://localhost:8080/recipes' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "Homemade Pizza",
"tags" : ["italian", "pizza", "dinner"],
"ingredients": [
"1 1/2 cups (355 ml) warm water (105°F-115°F)",
 "1 package (2 1/4 teaspoons) of active dry yeast",
 "3 3/4 cups (490 g) bread flour",
 "feta cheese, firm mozzarella cheese, grated"
 ],
"instructions": [
"Step 1.",
 "Step 2.",
 "Step 3."
 ]
}' | jq -r

## GET

curl -s --location --request GET 'http://localhost:8080/recipes' \
--header 'Content-Type: application/json'

## DELETE
curl -v -sX DELETE http://localhost:8080/recipes/c0283p3d0cvuglq85log | jq -r