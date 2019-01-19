<template>
  <div>
    <b-row>
      <b-col cols="5">
        <h2>Liitteet</h2>
      </b-col>
      <b-col>
        <label class="btn btn-secondary float-right">
          Lisää tiedostoja...
          <input
            class="fileinput"
            type="file"
            accept=".pdf"
            @input="addedFiles"
            ref="fileInput"
          >
        </label>
      </b-col>
    </b-row>
    <b-row>
      <b-btn
        v-for="(r, idx) in receipts"
        :key="r.id"
        variant="primary"
        @click="remove(idx)"
        class="badge-style"
        v-b-tooltip.hover
        title="Poista."
      >
        <strong>{{ r.file.name }}</strong>
      </b-btn>
      <div v-if="!receipts.length" class="placeholder">
        <h4>Ei lisättyjä liitteitä.</h4>
      </div>
    </b-row>
  </div>
</template>
<script>
export default {
  props: ['value'],
  data() {
    return {
      count: 0,
      receipts: [],
    };
  },
  methods: {
    input() {
      this.$emit('input', this.receipts.map(r => r.file));
    },
    addedFiles() {
      for (const file of this.$refs.fileInput.files) {
        this.receipts.push({ file, id: this.count });
        this.count += 1;
      }
      this.input();
    },
    remove(idx) {
      this.receipts.splice(idx, 1);
      this.input();
    },
  },
};
</script>
<style lang="scss" scoped>
.fileinput {
  width: 0.1px;
  height: 0.1px;
  overflow: hidden;
}
.badge-style {
  margin: 0.3em;
}
.badge-style:hover {
  background-color: #dc3545;
  transition: 0.5s ease;
}
.placeholder {
  width: 100%;
  text-align: center;
  color: gray;
}
.row {
  margin-bottom: 0.5em;
}
</style>
