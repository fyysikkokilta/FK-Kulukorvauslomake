<template>
    <b-container id="app" fluid>
        <b-row>
            <b-col col md="8" lg="6" offset-md="2" offset-lg="3">
                <b-jumbotron header="FK">
                    <h1>Kulu- ja matkakorvaus</h1>
                </b-jumbotron>
            </b-col>
        </b-row>
        <b-row>
            <b-col col md="8" lg="6" offset-md="2" offset-lg="3">
                <router-view />
            </b-col>
        </b-row>
    </b-container>
</template>
