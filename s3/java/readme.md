# create a new Maven project

```sh
mvn -B archetype:generate \
 -DarchetypeGroupId=software.amazon.awssdk \
 -DarchetypeArtifactId=archetype-lambda -Dservice=s3 -Dregion=eu-north-1 \
 -DarchetypeVersion=2.30.13 \
 -DgroupId=com.example.myapp \
 -DartifactId=myapp
```
