<template>
  <b-row style="margin-top: 5px;">
    <b-col col cols="3" md="4">
      <label for="distance-input">Matkan pituus</label>
    </b-col>
    <b-col col cols="8" md="7" lg="5" xl="4">
      <b-input-group prepend="km" append="€">
        <b-form-input id="distance-input" type="text" :value="value" required @input="input"/>
        <b-form-input readonly :value="visual"/>
      </b-input-group>
    </b-col>
    <img width="400" height="300" class="pie" src="pie.png" v-if="Math.abs(value - 3.1415927) < 0.0000005" />
  </b-row>
</template>
<script>
export default {
  props: ['value'],
  methods: {
    input(value) {
      this.$emit('input', value);
    },
  },
  computed: {
    visual() {
      return `= ${(this.value * 0.25).toFixed(2)}`;
    },
  },
};
</script>
<style lang="scss">
.pie {
  position: absolute;
  top: -200%;
  left: 10%;
  animation: flow 1s;
  opacity: 0;
}

@keyframes flow {
  0% {
    opacity: 0;
    top: -20%;
  }
  50% {
    opacity: 1;
    top: -20%;
  }
  100% {
    opacity: 0;
    top: -20%;
  }
}
</style>
