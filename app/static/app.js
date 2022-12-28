const h1 = document.getElementById('header__h1');
const mainDiv = document.getElementById('main__div');
const search = document.getElementById('search');

class Router {
  routes = [];
  mode = null;
  root = '/';

  constructor(options) {
    this.mode = window.history.pushState ? 'history' : 'hash';
    if (options.mode) this.mode = options.mode;
    if (options.root) this.root = options.root;
    this.listen();
  }

  add = (path, cb) => {
    this.routes.push({ path, cb });
    return this;
  };

  remove = (path) => {
    for (let i = 0; i < this.routes.length; i += 1) {
      if (this.routes[i].path === path) {
        this.routes.slice(i, 1);
        return this;
      }
    }
    return this;
  };

  flush = () => {
    this.routes = [];
    return this;
  };

  clearSlashes = (path) =>
    path.toString().replace(/\/$/, '').replace(/^\//, '');

  getFragment = () => {
    let fragment = '';
    if (this.mode === 'history') {
      fragment = this.clearSlashes(
        decodeURI(window.location.pathname + window.location.search)
      );
      fragment = fragment.replace(/\?(.*)$/, '');
      fragment = this.root !== '/' ? fragment.replace(this.root, '') : fragment;
    } else {
      const match = window.location.href.match(/#(.*)$/);
      fragment = match ? match[1] : '';
    }
    return this.clearSlashes(fragment);
  };

  navigate = (path = '') => {
    if (this.mode === 'history') {
      window.history.pushState(null, null, this.root + this.clearSlashes(path));
    } else {
      window.location.href = `${window.location.href.replace(
        /#(.*)$/,
        ''
      )}#${path}`;
    }
    return this;
  };

  listen = () => {
    clearInterval(this.interval);
    this.interval = setInterval(this.interval, 50);
  };

  interval = () => {
    if (this.current === this.getFragment()) return;
    this.current = this.getFragment();

    this.routes.some((route) => {
      const match = this.current.match(route.path);
      if (match) {
        match.shift();
        route.cb.apply({}, match);
        return match;
      }
      return false;
    });
  };
}

const router = new Router({
  mode: 'hash',
  root: '/',
});

router
  .add(/main_page/, () => {
    mainDiv.innerHTML = '';
    h1.textContent = 'Main page';
    mainDiv.style.marginRight = '1rem';
    search.style.display = 'none';
  })
  .add(/cameras_status/, () => {
    mainDiv.innerHTML = '';
    h1.textContent = 'Cameras status';
    mainDiv.style.marginRight = '30rem';
    search.style.display = '';
  })
  .add(/cabinets_status/, () => {
    mainDiv.innerHTML = '';
    h1.textContent = 'Cabinets status';
    mainDiv.style.marginRight = '30rem';
    search.style.display = '';
  })
  .add('', () => {
    // mainDiv.innerHTML = '';
    h1.textContent = 'Personal info';
    mainDiv.style.marginRight = '30rem';
    search.style.display = '';

    // const table = document.createElement('table');
    // const thead = document.createElement('thead');
    // const tbody = document.createElement('tbody');

    // table.appendChild(thead);
    // table.appendChild(tbody);

    // mainDiv.appendChild(table);

    // let row_1 = document.createElement('tr');
    // let heading_1 = document.createElement('th');
    // heading_1.innerHTML = 'Sr. No.';
    // let heading_2 = document.createElement('th');
    // heading_2.innerHTML = 'Name';
    // let heading_3 = document.createElement('th');
    // heading_3.innerHTML = 'Company';

    // row_1.appendChild(heading_1);
    // row_1.appendChild(heading_2);
    // row_1.appendChild(heading_3);
    // thead.appendChild(row_1);

    // let row_2 = document.createElement('tr');
    // let row_2_data_1 = document.createElement('td');
    // row_2_data_1.innerHTML = '1.';
    // let row_2_data_2 = document.createElement('td');
    // row_2_data_2.innerHTML = 'James Clerk';
    // let row_2_data_3 = document.createElement('td');
    // row_2_data_3.innerHTML = 'Netflix';

    // row_2.appendChild(row_2_data_1);
    // row_2.appendChild(row_2_data_2);
    // row_2.appendChild(row_2_data_3);
    // tbody.appendChild(row_2);

    // let row_3 = document.createElement('tr');
    // let row_3_data_1 = document.createElement('td');
    // row_3_data_1.innerHTML = '2.';
    // let row_3_data_2 = document.createElement('td');
    // row_3_data_2.innerHTML = 'Adam White';
    // let row_3_data_3 = document.createElement('td');
    // row_3_data_3.innerHTML = 'Microsoft';

    // row_3.appendChild(row_3_data_1);
    // row_3.appendChild(row_3_data_2);
    // row_3.appendChild(row_3_data_3);
    // tbody.appendChild(row_3);
  });

const urlPersonal = 'personal';
const urlUsers = 'users';
const urlCameras = 'cameras';
const urlCabinets = 'cabinets';
const urlTime = 'time';

async function getData(url) {
  await fetch(`http://192.168.0.101/api/${url}/`, {
    method: 'GET',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
      // 'Content-Type': 'application/x-www-form-urlencoded',
      // 'Access-Control-Allow-Origin': true,
    },
  })
    .then((response) => {
      response.json().then((data) => {
        return console.log(data); // удалить эту строку
      });
    })
    .catch((e) => {
      console.log(e);
    });
}

getData(urlPersonal);
// getData(urlUsers);
// getData(urlCameras);
// getData(urlCabinets);
// getData(urlTime);
