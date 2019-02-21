#! /usr/local/bin/python3

# USAGE: add_news title date body

def __main__(args):

news_bar = f"""
    <!-- News Bar -->
      <div class="container-fluid p-0 news-bar text-white">
        <div class="row p-0 m-0">
          <div class="col-sm-auto p-2 bg-dark">
            <div class="ecm-primary font-weight-bold text-center align-middle"> NEWS </div>
          </div>
          <div class="col-sm p-1 bg-lessdark">
            <a class="text-smaller text-white font-weight-light" href="news/index.html#news1"> Prof. Rupp promoted to associate professor  </a>
            <br>
            <small class="ecm-primary font-italic"> February 4, 2019 </small>
          </div>
          <div class="col-sm p-1 bg-dark">
            <a class="text-smaller text-white font-weight-light" href="news/index.html#news2"> Prof. Rupp to serve as associate editor for Journal of Materials Chemistry A  </a>
            <br>
            <small class="ecm-primary font-italic"> January 31, 2019 </small>
          </div>
          <div class="col-sm p-1 bg-lessdark">
            <a class="text-smaller text-white font-weight-light" href="news/index.html#news3"> Welcome Martin, Andrea, and Won Seok </a>
            <br>
            <small class="ecm-primary font-italic"> January 30, 2019 </small>
          </div>
        </div>
      </div>
    </div>    
"""  