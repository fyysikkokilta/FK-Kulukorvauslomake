<template>
  <b-container id="app" fluid>
    <b-toast id="submitted-toast" variant="success" solid>
      <div slot="toast-title">Kaikki on hyvin.</div>
      Lomakkeen lähetys onnistui.
    </b-toast>
    <b-toast id="error-toast" variant="danger" solid>
      <div slot="toast-title">Jotain meni pieleen...</div>
      Lomakkeen lähetys epäonnistui.
    </b-toast>
    <b-row>
      <b-col col md="8" lg="6" offset-md="2" offset-lg="3">
        <b-jumbotron header="FK">
          <h1 @dblclick="egg">Kulu- ja matkakorvaus</h1>
          <router-link v-if="!user" :to="{ path: '/login' }" class="float-right">Kirjaudu</router-link>
          <div v-else class="float-right">
            <router-link :to="{ name: 'view' }">Arkistoon</router-link>
            &nbsp;&nbsp;
            <router-link :to="{ name: 'home' }">Lomakkeeseen</router-link>
          </div>
        </b-jumbotron>
      </b-col>
    </b-row>
    <b-row>
      <b-col col md="8" lg="6" offset-md="2" offset-lg="3">
        <router-view/>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
import { mapActions, mapState, mapMutations } from 'vuex';
export default {
  computed: mapState(['user', 'message']),
  created() {
    // TODO make more generic toast
    const error = () => this.$bvToast.show('error-toast');
    const success = () => this.$bvToast.show('submitted-toast');
    console.log({ error, success });
    this.setCallbacks({ success, error });
  },
  methods: {
    ...mapActions(['fetchUser']),
    ...mapMutations(['setCallbacks']),
    egg() {
      window.location.href = `https://xkcd.com/${Math.floor(
        Math.random() * 2109,
      )}`;
    },
  },
  mounted() {
    this.fetchUser();
  },
};
</script>
