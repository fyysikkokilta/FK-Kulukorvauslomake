<template>
  <b-btn class="submit" @click="$emit('submit')" variant="success">Lähetä</b-btn>
</template>
<style lang="scss" scoped>
.submit {
  width: 100%;
  height: 3em;
  font-size: 1.5em;
}
</style>
