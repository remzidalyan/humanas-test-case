<<<<<<< HEAD
FROM node:18-alpine as builder

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

FROM node:18-alpine

WORKDIR /app

COPY --from=builder /app/package.json /app/package.json
COPY --from=builder /app/node_modules /app/node_modules
COPY --from=builder /app/build /app/build

RUN npm install -g serve

CMD ["serve", "-s", "build", "-l", "3000"]
=======
FROM node:18-alpine as builder

WORKDIR /app

COPY . .

RUN npm install
RUN npm run build

FROM node:18-alpine

WORKDIR /app

COPY --from=builder /app/package.json /app/package.json
COPY --from=builder /app/node_modules /app/node_modules
COPY --from=builder /app/build /app/build

RUN npm install -g serve

CMD ["serve", "-s", "build", "-l", "3000"]
>>>>>>> 6c728f5 (Conflict Resolve)
