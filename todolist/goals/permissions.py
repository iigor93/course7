from django.shortcuts import get_object_or_404

from goals.models import Board, BoardParticipant, Goal, GoalCategory

from rest_framework import permissions


class BoardPermissions(permissions.BasePermission):
    """Board permissions"""
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(user=request.user, board=obj).exists()
        if request.method == 'DELETE':
            return BoardParticipant.objects.filter(user=request.user, board=obj,
                                                   role=BoardParticipant.Role.OWNER).exists()
                                    
        return BoardParticipant.objects.filter(user=request.user,
                                               board=obj,
                                               role__in=(BoardParticipant.Role.OWNER,
                                                         BoardParticipant.Role.WRITER)).exists()


class GoalCategoryCreatePermissions(permissions.BasePermission):
    """Category create permissions"""
    def has_permission(self, request, view):
        board_id = request.data.get('board')
        board = get_object_or_404(Board, pk=board_id)
        return BoardParticipant.objects.filter(user=request.user,
                                               board=board,
                                               role__in=(BoardParticipant.Role.OWNER,
                                                         BoardParticipant.Role.WRITER)).exists()


class GoalCategoryDetailPermissions(permissions.BasePermission):
    """Category detail permissions"""
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(user=request.user, board=obj.board).exists()
                            
        return BoardParticipant.objects.filter(user=request.user,
                                               board=obj.board,
                                               role__in=(BoardParticipant.Role.OWNER,
                                                         BoardParticipant.Role.WRITER)).exists()


class GoalPermissions(permissions.BasePermission):
    """Goal permission"""
    def has_permission(self, request, view):
        category_id = request.data.get('category')
        category = get_object_or_404(GoalCategory, pk=category_id)
        
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(user=request.user, board=category.board).exists()
        
        return BoardParticipant.objects.filter(user=request.user,
                                               board=category.board,
                                               role__in=(BoardParticipant.Role.OWNER,
                                                         BoardParticipant.Role.WRITER)).exists()


class GoalDetailPermissions(permissions.BasePermission):
    """Goal detail permissions"""
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(user=request.user, board=obj.category.board).exists()
                            
        return BoardParticipant.objects.filter(user=request.user,
                                               board=obj.category.board,
                                               role__in=(BoardParticipant.Role.OWNER,
                                                         BoardParticipant.Role.WRITER)).exists()


class GoalCommentCreatePermissions(permissions.BasePermission):
    """Comment create permissions"""
    def has_permission(self, request, view):
        goal_id = request.data.get('goal')
        goal = get_object_or_404(Goal, pk=goal_id)
        return BoardParticipant.objects.filter(user=request.user,
                                               board=goal.category.board,
                                               role__in=(BoardParticipant.Role.OWNER,
                                                         BoardParticipant.Role.WRITER)).exists()


class GoalCommentPermissions(permissions.BasePermission):
    """Comment permissions"""
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return BoardParticipant.objects.filter(user=request.user, board=obj.goal.category.board).exists()
                            
        return BoardParticipant.objects.filter(user=request.user,
                                               board=obj.goal.category.board,
                                               role__in=(BoardParticipant.Role.OWNER,
                                                         BoardParticipant.Role.WRITER)).exists()
