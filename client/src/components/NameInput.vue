<template>
    <b-row>
        <b-col cols="3" md="4">
            <label for="name-input">Nimi</label>
        </b-col>
        <b-col cols="9" md="8">
            <b-input
                id="name-input"
                type="text"
                :value="name"
                required
                placeholder="Matti Meikäläinen"
                @input="input"
            />
        </b-col>
    </b-row>
</template>
<script>
export default {
    props: ['value'],
    data() {
        return { name: localStorage.name };
    },
    methods: {
        input(value) {
            this.$emit('input', value);
            localStorage.name = value;
        },
    },
};
</script>
