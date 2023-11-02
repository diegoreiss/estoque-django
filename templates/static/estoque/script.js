const formCriarProduto = document.querySelector("#formCriarProduto");
const btnSairFormProduto = document.querySelector("#btn-sair-form-produto");

btnSairFormProduto.addEventListener("click", (e) => {
  formCriarProduto.reset();
});
