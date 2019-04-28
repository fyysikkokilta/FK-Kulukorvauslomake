import Vue from 'vue';
import Vuex from 'vuex';

import * as api from '@/api';
import router from '@/router';

Vue.use(Vuex);

// TODO maybe split into modules
// for user, view and send.
export default new Vuex.Store({
  state: {
    previousSearch: {},
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
    CLEAR_ERROR(state) {
      state.error = null;
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
        commit('CLEAR_ERROR');
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
    async fetchReimbursements({ commit, state }, search) {
      const params = search || state.previousSearch;
      state.previousSearch = params;
      commit('SET_LOADING', true);
      try {
        const { data: reimbursements } = await api.getReimbursements(params);
        commit('SET_REIMBURSEMENTS', reimbursements);
      } catch (e) {
        if (e.response && e.response.status === 401) {
          router.push({ path: '/login' });
        } else throw e;
      } finally {
        commit('SET_LOADING', false);
      }
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

      await api.sendCostReimbursement(transformedForm);

      commit('SET_LOADING', false);
    },
    async sendTravelReimbursement({ commit }, form) {
      commit('SET_LOADING', true);
      await api.sendTravelReimbursement(form);
      commit('SET_LOADING', false);
    },
    async updateReimbursement({ commit, dispatch }, { id, ...data }) {
      commit('SET_LOADING', true);
      try {
        await api.updateReimbursement(id, data);
      } finally {
        dispatch('fetchReimbursements', null);
      }
      commit('SET_LOADING', false);
    },
  },
});
