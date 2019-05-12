<template>
  <b-btn class="submit" @click="$emit('submit')" variant="success" :disabled="loading">
    Lähetä&nbsp;
    <fa-icon icon="spinner" pulse v-show="loading"/>
  </b-btn>
</template>
<script>
import { mapState } from 'vuex';
export default {
  computed: mapState(['loading']),
};
</script>

<style lang="scss" scoped>
.submit {
  width: 100%;
  height: 3em;
  font-size: 1.5em;
}
</style>
