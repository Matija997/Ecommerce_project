<template>
  <div class="admin-page">

    <h1>Admin Dashboard</h1>

    <div class="admin-cards">

      <div class="card">
        <h3>Products</h3>
        <button>
          Manage Products
        </button>
      </div>


      <div class="card">
        <h3>Users</h3>
        <button>
          Manage Users
        </button>
      </div>


      <div class="card">
        <h3>Orders</h3>
        <button>
          Manage Orders
        </button>
      </div>

    </div>

  </div>
</template>


<style scoped>

.admin-page {
    padding-top:100px;
    text-align:center;
}


.admin-cards {
    display:flex;
    justify-content:center;
    gap:30px;
}


.card {
    width:200px;
    padding:30px;
    border:1px solid #ddd;
    border-radius:10px;
}


</style>