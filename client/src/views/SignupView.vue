<template>
  <div class="signup">
    <section class="vh-100 gradient-custom">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card bg-dark text-white" style="border-radius: 1rem">
              <div class="card-body p-5 text-center">
                <div class="mb-md-5 mt-md-4 pb-5">
                  <h2 class="fw-bold mb-2 text-uppercase">SignUp</h2>
                  <p class="text-white-50 mb-5">
                    회원가입을 위한 정보들을 입력해주세요.
                  </p>
                  <form @submit.prevent="signUp">
                    <div class="form-outline form-white mb-4">
                      <input
                        type="text"
                        id="username"
                        v-model="username"
                        class="form-control form-control-lg"
                        placeholder="아이디"
                      />
                    </div>

                    <div class="form-outline form-white mb-4">
                      <input
                        type="password"
                        id="password1"
                        v-model="password1"
                        class="form-control form-control-lg"
                        placeholder="비밀번호"
                      />
                    </div>

                    <div class="form-outline form-white mb-4">
                      <input
                        type="password"
                        id="password2"
                        v-model="password2"
                        class="form-control form-control-lg"
                        placeholder="비밀번호 확인"
                      />
                    </div>

                    <div class="form-outline form-white mb-4">
                      <input
                        type="email"
                        id="email"
                        v-model="email"
                        class="form-control form-control-lg"
                        placeholder="이메일"
                      />
                    </div>

                    <button
                      class="btn btn-outline-light btn-lg px-5"
                      type="submit"
                    >
                      회원가입
                    </button>
                  </form>
                  <!-- <div
                    class="d-flex justify-content-center text-center mt-4 pt-1"
                  >
                    <a href="#!" class="text-white"
                      ><i class="fab fa-facebook-f fa-lg"></i
                    ></a>
                    <a href="#!" class="text-white"
                      ><i class="fab fa-twitter fa-lg mx-4 px-2"></i
                    ></a>
                    <a href="#!" class="text-white"
                      ><i class="fab fa-google fa-lg"></i
                    ></a>
                  </div> -->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: "",
      password1: "",
      password2: "",
      email: "",
    };
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const email = this.email

      const payload = {
        username, password1, password2, email
      }
      this.$store.dispatch('signUp',payload)
    },
  },
};
</script>
<style scoped>
.gradient-custom {
  /* fallback for old browsers */
  background: #6a11cb;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(
    to right,
    rgba(106, 17, 203, 1),
    rgba(37, 117, 252, 1)
  );
}
</style>
