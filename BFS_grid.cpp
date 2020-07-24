
    vivi dist(h,vi(w,INF));
    QP q;
    q.push(make_pair(sy,sx));
    dist[sy][sx] = 0;
    while(!q.empty()) {
      int cy=q.front().first,cx=q.front().second;
      q.pop();
      REP(i,4) {
        int ex=cx+dx[i],ey=cy+dy[i];
        if(ex<0||ex>=w||ey<0||ey>=h) continue;
        if(dist[ey][ex]!=INF||c[ey][ex]=='X') continue;
        dist[ey][ex]=dist[cy][cx]+1;
        q.push(make_pair(ey,ex));
      }
    }
    ans=dist[gy][gx];