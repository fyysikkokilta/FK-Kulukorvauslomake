<template>
  <div>
    <b-row>
      <b-col cols="10">
        <h2>Erittelyt</h2>
      </b-col>
      <b-col>
        <b-btn class="float-right" @click="add">+</b-btn>
      </b-col>
    </b-row>
    <SingleExplanationsInput
      v-for="(exp, idx) in explanations"
      :key="exp.id"
      v-model="explanations[idx]"
      @input="input"
      @remove="remove(idx)"
    />
  </div>
</template>
<script>
import SingleExplanationsInput from '@/components/SingleExplanationsInput.vue';

export default {
  components: { SingleExplanationsInput },
  props: ['value'],
  data() {
    return {
      count: 1,
      explanations: [{ amount: null, explanation: '', id: 0 }],
    };
  },
  methods: {
    add() {
      this.explanations.push({
        amount: null,
        explanation: '',
        id: this.count,
      });
      this.count += 1;
      this.input();
    },
    input() {
      this.$emit(
        'input',
        this.explanations.map(exp => ({
          explanation: exp.explanation,
          amount: exp.amount,
        })),
      );
    },
    remove(idx) {
      this.explanations.splice(idx, 1);
      this.input();
    },
  },
};
</script>
