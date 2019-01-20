import Vue from 'vue';
import Vuex from 'vuex';

import * as api from '@/api';
import router from '@/router';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loading: false,
    user: null,
    error: null,
    reimbursements: {
      data: [],
      pages: 0,
    },
  },
  getters: {
    pages: state => {
      return state.reimbursements.pages;
    },
  },
  mutations: {
    SET_LOADING(state, status) {
      state.loading = status;
    },
    SET_USER(state, user) {
      state.user = user;
    },
    SET_ERROR(state, error) {
      state.error = error;
    },
    SET_REIMBURSEMENTS(state, data) {
      state.reimbursements = data;
    },
  },
  actions: {
    async fetchUser({ commit }) {
      try {
        const { data: user } = await api.me();
        commit('SET_USER', user);
      } catch (e) {
        if (e.response.status !== 401) {
          throw e;
        }
      }
    },
    async login({ commit, dispatch }, { email, password }) {
      try {
        commit('SET_LOADING', true);

        await api.login(email, password);
        await dispatch('fetchUser');

        commit('SET_ERROR', null);
        router.push({ name: 'view' });
      } catch (e) {
        if (!e.response) throw e;

        if (e.response.status === 401) {
          commit('SET_ERROR', 'Tarksita sähköposti ja salasana.');
        } else throw e;
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchReimbursements({ commit }, search) {
      const { data: reimbursements } = await api.getReimbursements(search);
      commit('SET_REIMBURSEMENTS', reimbursements);
    },
    async sendCostReimbursement({ commit }, form) {
      commit('SET_LOADING', true);

      // There is probably some library that simplifies this
      const receipts = await Promise.all(
        form.receipts.map(
          r =>
            new Promise(resolve => {
              const fr = new FileReader();

              fr.onload = e => {
                resolve({
                  content: e.target.result,
                  originalName: r.name,
                });
              };
              fr.readAsDataURL(r);
            }),
        ),
      );

      const explanations = form.explanations.map(exp => ({
        explanation: exp.explanation,
        amount: exp.amount,
      }));

      const transformedForm = {
        ...form,
        receipts,
        explanations,
      };

      const resp = await api.sendCostReimbursement(transformedForm);
      console.log(resp);

      commit('SET_LOADING', false);
    },
  },
});
