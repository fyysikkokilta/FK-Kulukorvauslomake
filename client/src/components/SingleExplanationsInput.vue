<template>
  <b-row>
    <b-col cols="7">
      <b-input-group prepend="Kuvaus">
        <b-form-textarea v-model="explanation" @input="input" required/>
      </b-input-group>
    </b-col>
    <b-col cols="3">
      <b-input-group append="€">
        <b-form-input
          v-model="amount"
          placeholder="5.00"
          type="number"
          min="0.00"
          @input="input"
          required
        />
      </b-input-group>
    </b-col>
    <b-col>
      <b-btn variant="danger" class="float-right" @click="$emit('remove')">-</b-btn>
    </b-col>
  </b-row>
</template>
<script>
export default {
  props: ['value'],
  data() {
    return {
      amount: null,
      explanation: '',
    };
  },
  methods: {
    input() {
      this.$emit('input', {
        amount: +this.amount,
        explanation: this.explanation,
        id: +this.value.id,
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.row {
  margin-bottom: 0.5em;
}
div[class^='col-'] {
  padding-left: 5px;
  padding-right: 5px;
}
.btn {
  width: 36px;
}
</style>
