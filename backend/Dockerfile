FROM maven:3.9-eclipse-temurin-17 AS build
WORKDIR /app
COPY maven-mirror-settings.xml /tmp/mirror-settings.xml

# Maven Central sometimes returns HTTP 429 to shared build servers.
# mvn_retry tries Maven Central, then a Google mirror, up to 8 attempts.
RUN printf '%s\n' \
  '#!/bin/sh' \
  'i=1' \
  'while [ "$i" -le 8 ]; do' \
  '  if [ $((i % 2)) -eq 1 ]; then' \
  '    mvn -q -B "$@" && exit 0' \
  '  else' \
  '    mvn -q -B -s /tmp/mirror-settings.xml "$@" && exit 0' \
  '  fi' \
  '  echo "Maven attempt $i failed, retrying in $((i * 10))s..."' \
  '  sleep $((i * 10))' \
  '  i=$((i + 1))' \
  'done' \
  'exit 1' > /usr/local/bin/mvn_retry && chmod +x /usr/local/bin/mvn_retry

COPY pom.xml .
RUN mvn_retry dependency:go-offline
COPY src ./src
RUN mvn_retry clean package -DskipTests

FROM eclipse-temurin:17-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
ENV SPRING_PROFILES_ACTIVE=prod \
    JAVA_TOOL_OPTIONS="-Xmx384m"
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
