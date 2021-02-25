import './App.css';

function App() {
  return (
    <div className="App" style={{marginLeft:"40px",marginRight:"40px"}}>
      <h1>Ecommerce site</h1>
      <div style={{marginTop:"30px"}}>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="/#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="/#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-link active" href="/#">Home <span class="sr-only">(current)</span></a>
      <a class="nav-link" href="/#">Features</a>
      <a class="nav-link" href="/#">Pricing</a>
      <a class="nav-link disabled" href="/#" tabindex="-1" aria-disabled="true">Disabled</a>
    </div>
  </div>
</nav>
</div>
<div id="carouselExampleFade" class="carousel slide carousel-fade" data-ride="carousel" style={{height:"420px", width:"100px"}}>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://picsum.photos/200/300" class="d-block w-100" alt="..."/>
    </div>
    <div class="carousel-item">
      <img src="https://picsum.photos/200/300" class="d-block w-100" alt="..."/>
    </div>
    <div class="carousel-item">
      <img src="https://picsum.photos/200/300" class="d-block w-100" alt="..."/>
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleFade" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleFade" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<div style={{marginTop:"20px"}}/>
      <div class="card" style={{width: "18rem"}}>
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="/#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
      </div>
  );
}

export default App;
