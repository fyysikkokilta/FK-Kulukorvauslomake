<template>
  <b-row style="margin-top: 5px;">
    <b-col col cols="3" md="4">
      <label for="license-input">Ajoneuvon rekisterinumero</label>
    </b-col>
    <b-col col cols="8" md="7" lg="5" xl="4">
      <b-input
        id="license-input"
        type="text"
        :value="value"
        required
        @input="input"
      />
    </b-col>
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
};
</script>
